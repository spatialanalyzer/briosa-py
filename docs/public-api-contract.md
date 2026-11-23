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

The first exact-target distribution is `briosa-2026-1-0529-7`. Future SA
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
  `dataclasses.replace()`. A named value that a caller passes explicitly, such
  as `ToleranceVectorOptions.NO_LIMITS`, is never an implicit default.
- An optional input with no reviewed default is `T | None = None` and leaves its
  protobuf field unset when omitted. An omitted optional list that maps to a
  plain repeated field is sent empty, its absent value on the wire. The client
  never sends an empty value, 0, or false for an argument the caller left unset.
- An input the server requires is required: it has no default and is not
  `T | None`, and the client never fills it in with an identity transform, a
  default settings value, an empty list or a default choice. Omitting one fails
  with `TypeError` before any call. An input stays optional only when the server
  accepts it absent.
- Every MP method takes the keyword-only call control
  `on_mp_completion: MpCompletionObserver | None = None` (Server 0.10.x). The
  client checks every MP success, observed or not: its execution details must
  pair `SUCCEEDED` with MP code 2 or `PARTIAL_SUCCESS` with code 4, and anything
  else, including a missing code, is `BriosaProtocolError`
  (`mp-completion-invalid`). The client then calls the observer once with that
  `MpCompletion`, before it maps the outputs, so the observer also hears of a
  success whose outputs fail to map. A partial success (MP code 4) is a
  success: the method returns its outputs when all of them are retrieved, and
  never retries. A failed call reports no completion; its typed failure carries
  the MP execution details instead. After code 4, a call whose output can't be
  retrieved fails with `OUTPUT_RETRIEVAL_FAILURE`, or `SDK_CALL_FAULTED` when a
  getter raised, and its details keep `PARTIAL_SUCCESS` with code 4. Their
  output retrievals are the per-output states the server reports, which don't
  always identify the getter. Return types never change.

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
- Every `OperationFailureKind` value is its own member, including
  `SDK_CALL_FAULTED`; the execution disposition carries its phase.
  `OperationFailure.mp_execution` keeps `PARTIAL_SUCCESS` distinct inside a
  typed failure.
- A caller's own interruption is reported the native way: task cancellation as
  `asyncio.CancelledError`, and a `timeout` or `command_timeout` as
  `BriosaTransportError` with `transport-deadline-exceeded`. When a lifecycle
  detail does arrive with `CALLER_CANCELLED` or `CALLER_DEADLINE_EXCEEDED`, it is
  the typed lifecycle error with that kind, never a state conflict, and the
  client never retries it.

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

From client 0.5.1, an omitted `startup_timeout` follows the server's published
lifecycle bounds, which Server 0.10.1 and later report in
`BriosaServerSnapshot.lifecycle_bounds`. The budget runs on the event loop's
monotonic clock from one start instant, before the server is launched, and the
client adopts the allowance once, at the first verified server snapshot:

- the allowance is `startup_with_launch` for Start SDK, Launch, and Connect;
  `startup_without_launch` for Start SDK and Connect; `start_sdk` plus
  `launch_spatial_analyzer` for Start SDK and Launch; `start_sdk` or
  `launch_spatial_analyzer` alone for one phase; and none for a control-plane
  start. If any allowance the selection needs is unavailable, the budget stays
  at two minutes; a partial budget is never summed;
- the deadline becomes the start instant plus the larger of two minutes and
  the allowance plus 20 seconds, so adoption only ever lengthens the budget and
  the time already spent counts;
- a budget that has already run out when the snapshot arrives is never
  extended, and no further phase starts; the client keeps the current deadline
  when the new one cannot be scheduled; and
- no budget restarts at the snapshot after Connect, and caller cancellation
  stays independent.

An explicit `startup_timeout`, including `120.0`, is always used as given.
Only constructing the options without the argument omits it: the field reads as
a plain `float`, so a value passed back, however obtained, is explicit, and
`dataclasses.replace()` passes the budget explicitly. Copies and pickles keep
the omission, and equality and hashing compare values as in 0.5.0. Subclasses
of `BriosaStartOptions` keep the 0.5.0 behaviour and do not take the server's
published startup allowance. Against Server 0.10.0, which publishes no bounds,
an omitted budget stays at two minutes
and every startup step runs as in client 0.5.0. With a server that publishes
bounds, the client reads the clock and the startup's cancellation before it
takes ownership of the session, before it reports success, and for each startup
request after the request is built and immediately before it is sent. A startup
whose budget ran out, or that was cancelled, therefore sends no further request
and never reports success, even when its timer has not yet run. A request that
fails once the budget ran out raises `startup-timeout` with that failure as its
`__cause__`; one that fails earlier keeps its own error, including a
`TimeoutError` of its own. If such a startup fails after the client took
ownership, that session admits no MP call again; `stop()` and then `start()`
begin a new one. A cleanup failure after a failed startup becomes a note on the
startup's error instead of replacing it. When the timer ends the startup, expiry
raises `BriosaStartupError` (`startup-timeout`) chained to the same
`TimeoutError` as with client 0.5.0, because each Python version times the
startup as its `asyncio.wait_for` did for 0.5.0; on Python 3.10 the error also
derives from `asyncio.TimeoutError`.

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

When the lifecycle bounds of a server that publishes none, such as Server
0.10.0, are raised, or when you pass an explicit budget, size the client budget
to at least three times `StartupTimeout`, plus `ReadinessProbeTimeout`, plus
`ApplicationStartupTimeout` when launching, plus 10 s, plus a margin. For
example, a server `StartupTimeout` of 30 s and `ReadinessProbeTimeout` of 60 s
with the default 30 s application startup need at least 90 + 60 + 30 + 10 =
190 s, or 210 s (3.5 minutes) with the 20-second margin.

Each lifecycle method takes a keyword-only `timeout: float | None = None`. The
client sends a gRPC deadline only when the caller supplies one, and
`command_timeout` applies only to MP commands.

Server 0.10.x finishes an SDK start, connection, or recovery it
has accepted under its own bounds
([spatialanalyzer/briosa#315](https://github.com/spatialanalyzer/briosa/pull/315)),
whether the caller stopped waiting through the startup budget, a `timeout`, or
task cancellation. A start the client abandoned may therefore still produce a
ready generation. Refresh SDK state with `get_spatial_analyzer_sdk_state()`
before deciding what to do next, and call `get_server_snapshot()` to reopen MP
calls on a generation that became ready. The exception is a session whose
startup failed after the client took ownership while a server that publishes
lifecycle bounds (Server 0.10.1 and later) was guarding it: that session never
admits MP calls again, so call `stop()` and then `start()`. A second lifecycle
call during the
accepted transition fails with `sdk-lifecycle-transition-in-progress`
(`STATE_CONFLICT`, `REFRESH_STATE`): refresh and retry later, and stop a
generation you own only after the transition has ended. The same applies to
`launch_spatial_analyzer`
([#356](https://github.com/spatialanalyzer/briosa/pull/356)): after a launch
timeout, refresh application state before launching again.

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
Close.

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

## Implemented targets

Independent SA `2024.1.0508.5` and `2026.1.0529.7` products live under
`targets/`. See the [repository guide](../README.md) for package selection.
The target README records signature differences and validation limits.
