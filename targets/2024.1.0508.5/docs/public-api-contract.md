# Briosa Python public API contract

- Status: Accepted Python v1 design target; lifecycle foundation conforming
- Last reviewed: 2026-08-12

## Authority and scope

The [first-party client behavioral contract](https://github.com/spatialanalyzer/briosa/blob/main/docs/architecture/client-library-behavioral-contract.md)
is authoritative for behavior shared by the .NET, Python, and JavaScript/TypeScript
clients. The Briosa server, its public protocol, and the exact target-qualified
protocol artifact recorded in [`protocol.lock.json`](../protocol.lock.json) remain
authoritative for MP commands, inputs, outputs, presence, fixed defaults, typed
failures, compatibility coordinates, capabilities, execution disposition, and
replay safety.

This document records only how `briosa-py` expresses that shared contract as an
idiomatic Python API. It does not copy or redefine shared policy. The Python
choices were reviewed rule by rule and accepted in
[Discussion #6](https://github.com/orgs/spatialanalyzer/discussions/6#discussioncomment-17926452).

### Package and import identity

The first exact-target distribution is `briosa-2024-1-0508-5`. Future SA
targets use distinct distribution names while retaining the stable `briosa`
import package. Different target distributions therefore belong in separate
Python environments or processes rather than one environment with a runtime
target selector.

## Accepted Python decisions

### Client and command surface

- One application-scoped, handwritten `BriosaClient` is the flat public command
  surface. MP categories may organize implementation and documentation but do not
  appear in the ordinary call path.
- Each MP command has one canonical `async def` method. The exact MP name is
  transformed mechanically to `snake_case`, retaining every word and
  abbreviation and adding no `_async` suffix. Python keywords gain a trailing
  underscore, and normalized-name collisions require explicit review.
- MP inputs are direct Python parameters, not generated request envelopes.
  Parameter identity and order follow the MP contract; optional and defaulted MP
  inputs are keyword-only.
- Transport and asynchronous controls do not become MP parameters. The immutable
  `BriosaClientOptions` has a client-wide
  `command_timeout: float | None = None`; startup has its own timeout, and a
  one-off caller deadline or cancellation uses normal asyncio facilities.

### Public values and results

- Public domain models are handwritten, normally frozen and slotted dataclasses.
  Public enums are handwritten and mapped explicitly to wire values. A wire-only
  `UNSPECIFIED` member is omitted unless it has reviewed domain meaning.
- A command with no output returns `None`, one output returns that value directly,
  and multiple outputs return one named result. Named results are final, frozen,
  slotted, keyword-only dataclasses with public constructors. Prefer a domain name;
  otherwise use `MechanicalCommandNameResult`.
- A semantic optional output uses `T | None`. `None` is not a substitute for an
  empty or default-like value, and a missing required-on-success output is a
  protocol-contract failure.
- Collection inputs accept finite `Iterable[T]` values. The client consumes an
  iterable once and materializes it before starting the RPC. Collection outputs
  are fresh detached `list[T]` values; a present empty collection is `[]`, not
  `None`. A frozen result containing a list is intentionally only shallowly
  immutable.
- Reviewed scalar defaults appear directly in keyword-only signatures and are
  sent explicitly. Structured defaults are named, deeply immutable domain
  constants; callers derive modified dataclass values with
  `dataclasses.replace()`.

### Errors

- The handwritten hierarchy is rooted at `BriosaError`.
  `BriosaOperationError` represents a valid typed Briosa operation failure, while
  `BriosaTransportError` represents a transport failure without a valid typed
  detail. Lifecycle and compatibility failures have separate handwritten types.
- Public failures expose handwritten `OperationFailure` and `RpcStatusCode`
  values. `RpcStatusCode` covers every canonical gRPC status without exposing
  `grpc.StatusCode`; generated error messages and transport metadata are also
  private.
- Local argument failures use normal `TypeError` or `ValueError`.
  `asyncio.CancelledError` propagates normally. A diagnostic gRPC exception may
  be retained through Python's conventional `__cause__` without becoming part of
  policy or the public value model.

### Lifecycle and concurrency

- Constructing `BriosaClientOptions` or `BriosaClient` is dormant. It does not
  create a channel, perform an RPC, launch a process, probe readiness, or bind the
  client to an event loop.
- `await client.start()` establishes the verified generation required by the
  shared contract. Calling an MP command without an active generation raises
  `BriosaLifecycleError`; commands never start the client implicitly.
- `await client.stop()` ends the active generation and leaves the client reusable.
  `await client.aclose()` performs final asynchronous cleanup and permanently
  closes it. Both are safe after cleanup has already occurred.
- `async with BriosaClient(options)` is the canonical lifecycle convenience:
  entering calls `start()` and exiting calls `aclose()`.
- The first `start()` binds the client to its owning event loop. Concurrent tasks
  on that loop are supported, but the API makes no cross-thread or
  cross-event-loop guarantee and promises neither command ordering nor client-side
  serialization.

The canonical shape is:

```python
options = BriosaClientOptions(
    command_timeout=None,
)

async with BriosaClient(options) as client:
    working_directory = await client.get_working_directory()
```

The snippet is the implemented lifecycle shape. Endpoint selection remains a
private local-server concern rather than a public startup option.

### Startup and lifecycle time budgets

`BriosaStartOptions.startup_timeout` is one overall budget, in seconds, for the
whole `start()`, whichever phases are selected. It defaults to `120.0` (two
minutes). When it expires, `start()` raises `BriosaStartupError` with diagnostic
`startup-timeout`, whichever phase it interrupts, including an RPC in flight.
Cancelling the task that awaits `start()` only stops that caller from waiting and
raises `asyncio.CancelledError`; the start continues until it completes or its
budget expires.

The default follows the server's default lifecycle bounds
([spatialanalyzer/briosa#298](https://github.com/spatialanalyzer/briosa/pull/298),
[#315](https://github.com/spatialanalyzer/briosa/pull/315)) for the ordinary
start:

| Startup phase | Server bound (default) | Worst case until the server answers |
| --- | --- | --- |
| Launch the owned server and wait for discovery | none; server host startup | a few seconds |
| Start the SDK | `Briosa:Worker:StartupTimeout` (10 s), then 5 s cleanup on failure | 10 s (15 s on failure) |
| Launch SpatialAnalyzer | `Briosa:SpatialAnalyzer:ApplicationStartupTimeout` (30 s) | 30 s |
| Connect and prove readiness | ConnectEx and the application association, each under `Briosa:Worker:StartupTimeout` (10 s); the readiness probe under `Briosa:Worker:ReadinessProbeTimeout` (30 s); a 5 s liveness check; 5 s cleanup on failure | 55 s (60 s on failure) |
| Total | | 95 s to readiness, 100 s to a typed failure |

Two minutes leaves 20 seconds for server host startup, process observation,
installation discovery, and round trips. Attaching to a running SpatialAnalyzer
skips the 30-second launch. A heavily loaded machine can slow process
observation further until
[spatialanalyzer/briosa#317](https://github.com/spatialanalyzer/briosa/issues/317)
lands.

Released 0.9 servers and the pinned protocol build `89b59aa` have no larger
defaults: their startup bound is a fixed 10 s, and their readiness probe uses the
quick execution budget (30 s by default), so the default covers them too.

When the server's lifecycle bounds are raised, size the client budget to at
least three times `StartupTimeout`, plus `ReadinessProbeTimeout`, plus
`ApplicationStartupTimeout` when launching, plus 10 s, plus a margin. For
example, a server `StartupTimeout` of 30 s and `ReadinessProbeTimeout` of 60 s
with the default 30 s application startup need at least 90 + 60 + 30 + 10 =
190 s, or 210 s (3.5 minutes) with the 20-second margin.

Each lifecycle method takes a keyword-only `timeout: float | None = None`. The
client sends a gRPC deadline only when the caller supplies one, and
`command_timeout` applies only to MP commands.

What happens on the server when a caller stops waiting during an SDK start,
connection, or recovery depends on the server build:

- Builds that contain
  [spatialanalyzer/briosa#315](https://github.com/spatialanalyzer/briosa/pull/315)
  (briosa main from `0c7ff7a`, planned for the contract-major-3 release) finish
  an exchange they have accepted under their own bounds, whether the caller
  stopped waiting through the startup budget, a `timeout`, or task cancellation.
- Older supported builds, including every released 0.9 server and the pinned
  protocol build `89b59aa`, cancel the exchange with the caller. A cancelled SDK
  start, or the replacement start inside a recovery, terminates the new worker
  and leaves the SDK stopped (`worker-startup-cancelled`). A cancelled ConnectEx
  retires the generation, which then needs recovery (`connect-ex-cancelled`). A
  cancelled readiness probe quarantines the generation and requires operator
  recovery (`execution-readiness-probe-cancelled`).

Either way, refresh SDK state before deciding what to do next.

A lifecycle `timeout` shorter than the server's worst case for that call can
stop the caller waiting before the server's typed failure, lifecycle state, and
recovery guidance arrive. Under the default server configuration, use at least
the deadlines below. Each is the server's worst case to a typed answer, failure
cleanup included, plus 5 s for scheduling, transport, and an idle process
observation. Allow more on a heavily loaded machine.

| Call | Server worst case to a typed answer | Minimum per-call deadline |
| --- | --- | --- |
| Start the SDK | 15 s: the 10 s startup bound, then up to 5 s of worker cleanup on failure | 20 s |
| Connect or reconnect | 60 s: ConnectEx 10 s, readiness probe 30 s, application association 10 s, and liveness check 5 s, then up to 5 s of worker cleanup on failure; a process observation comes first | 65 s |
| Recover the SDK | 25 s: heartbeat drain 5 s, cleanup of the faulted worker 5 s, and replacement start 10 s, then up to 5 s of worker cleanup on failure | 30 s |
| Launch SpatialAnalyzer | 30 s: the application startup bound, after a process observation | 35 s |
| Close the owned SpatialAnalyzer | 30 s: the application shutdown bound, with up to two process observations | 35 s |
| Stop the SDK | the execution budget of any in-flight MP command, then 15 s: heartbeat drain 5 s, stop exchange 5 s, and forced cleanup 5 s | that budget + 20 s |

When the server's bounds are raised, add the increase: `StartupTimeout` counts
once for Start and Recover and twice for Connect, `ReadinessProbeTimeout` once
for Connect, and the application startup and shutdown bounds once for Launch and
Close. Released 0.9 servers and the pinned build `89b59aa` have the same or
shorter worst cases, with one exception: they associate the application after
Connect reports readiness, so Connect can also wait behind an MP command that
another client submits in between.

## Deferred design decisions

The following details are deliberately not settled by this repository contract:

- Runtime ownership modes, artifact discovery, endpoint selection, concurrent
  lifecycle-call behavior, and partial-startup cleanup follow the central
  lifecycle design tracked by
  [`briosa` issue #147](https://github.com/spatialanalyzer/briosa/issues/147).
- Exact domain types, validation rules, fixed defaults, and output optionality for
  a command are decided only with that command's reviewed server and protocol
  slice. They are not inferred locally from generated method names or wire
  defaults.
- A domain type that is not naturally represented by a dataclass requires an
  explicit Python API review; "normally a dataclass" is not permission to invent
  a representation before its command slice is reviewed.
- The private generated-code layout may change during the pre-v1 migration. Its
  current import path is not a compatibility promise.

An ambiguity in shared behavior is resolved in `spatialanalyzer/briosa` before a
Python implementation proceeds. This document cannot create a Python-only
exception to the shared safety contract.

## Implemented Lifecycle Foundation

The package now uses dormant construction, explicit reusable asynchronous
lifecycle, async context management, private generated transport, handwritten
public states and errors, Python-native cancellation, exact-target compatibility
checks, and detached MP results required by this contract. Subsequent vertical
slices add handwritten MP methods without changing this lifecycle foundation.

## Python v1 non-goals

In addition to the non-goals inherited from the shared contract, `briosa-py` v1
does not provide:

- synchronous command or lifecycle wrappers, including wrappers that call
  `asyncio.run()`;
- `_async` aliases, category clients, convenience command aliases, or other
  duplicate MP entry points;
- a supported raw generated protobuf/gRPC surface inside the exact-target
  distribution;
- cross-thread or cross-event-loop use, implicit command ordering, or a promise of
  parallel SpatialAnalyzer execution; or
- runtime deep-freezing of detached lists stored in frozen result dataclasses.

Changes to shared behavior begin in `spatialanalyzer/briosa`. Changes to an
accepted Python expression require a reviewed `briosa-py` issue and update this
document before implementation treats the new shape as normative.
