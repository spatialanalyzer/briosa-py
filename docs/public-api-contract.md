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
- a supported raw generated protobuf/gRPC surface inside `briosa-client`;
- cross-thread or cross-event-loop use, implicit command ordering, or a promise of
  parallel SpatialAnalyzer execution; or
- runtime deep-freezing of detached lists stored in frozen result dataclasses.

Changes to shared behavior begin in `spatialanalyzer/briosa`. Changes to an
accepted Python expression require a reviewed `briosa-py` issue and update this
document before implementation treats the new shape as normative.
