# Briosa Python clients

[Documentation](https://briosa.dev/) | [API Reference](https://briosa.dev/api/python) | [First MP Command](https://briosa.dev/docs/getting-started/first-request)

Independent exact-target clients for the [Briosa SpatialAnalyzer bridge](https://github.com/spatialanalyzer/briosa).

| SpatialAnalyzer target | Product and development guide | Client version |
| --- | --- | --- |
| 2024.1.0508.5 | [SA 2024](targets/2024.1.0508.5/README.md) | 0.5.1 |
| 2026.1.0529.7 | [SA 2026](targets/2026.1.0529.7/README.md) | 0.5.1 |

Choose the package for your exact SA installation. Client 0.5.x works with
Server 0.10.x (Client 0.5.0 was tested with Server 0.10.0; Client 0.5.1 was
tested with Server 0.10.0 and with the Server 0.10.1 protocol checkpoint
`0.10.1-dev.1`) and does not work with Server 0.9.x and earlier; clients 0.4.x
and earlier do not work with Server 0.10.x. For server releases after 0.10.0, a
patch update keeps the same clients working; a minor update may require a
client upgrade. Each product pins its own generation artifact and retains
Server 0.9.2, the latest 0.9.x server, as the rejection baseline. Each product
guide lists the additions that arrive with Server 0.10.1 under "New in 0.5.1
(Server 0.10.1)" and the 0.5.0 breaking changes under "Upgrading to 0.5.0
(Server 0.10.x)". Client package versions are independent of the Briosa server
version. See [Releasing](RELEASING.md) for registry publishing and validation.

Package names include the SA target; application namespaces/imports remain stable.
See each product guide for installation and examples. Run development commands
from the chosen `targets/<exact-sa-release>/` directory. CI validates both products.

SpatialAnalyzer, its SDK, and a license are required separately for real work.
Portable checks do not establish licensed runtime validation. Broader licensed
runtime CI and enterprise Artifactory verification remain outstanding before v1.0
promotion.

The 0.3.0 API naming changes are described in the [MP argument migration guide](docs/mp-argument-name-migration.md).

The default `BriosaStartOptions.startup_timeout` is `120.0` seconds in both
products. It is sized from the server's default lifecycle bounds. With Server
0.10.1 and later, an omitted budget follows the server's published startup
allowance and is never less than 120 seconds; against Server 0.10.0 it stays at
120 seconds. An explicit value is always used as given. If a startup against
a server that publishes lifecycle bounds fails after the client took ownership
of the session, that session admits no MP command for the rest of its life,
whatever later state reads report; call `stop()` and then `start()` to begin a
new one. See
[startup and lifecycle time budgets](docs/public-api-contract.md#startup-and-lifecycle-time-budgets).

**Compatibility with client 0.5.0.** Guaranteed for an application written for
client 0.5.0:

- Every public name and signature of 0.5.0 is still there; client 0.5.1 only
  adds names, and keyword-only parameters with defaults.
- Against Server 0.10.0, ordinary use behaves as with 0.5.0, with two
  differences, both on Python 3.10 only: a startup timeout is now a
  `BriosaStartupError` that is also an `asyncio.TimeoutError`, so
  `type(e) is asyncio.TimeoutError` is no longer true; and a `stop()` during a
  hung startup now closes the client's resources on the first call.
- Objects of Briosa's own value types that 0.5.0 pickled load in 0.5.1.
- `repr()`, equality and hashing of those types are unchanged.
- Subclasses of `BriosaStartOptions` behave as in 0.5.0: a subclass's startup
  always uses its own `startup_timeout`, never the server's published startup
  allowance.

Not guaranteed; known differences from 0.5.0:

- `dataclasses.fields()`, `astuple()` and `asdict()` on `OperationFailure`,
  `BriosaOperationCapability` and `BriosaServerSnapshot` include the fields
  0.5.1 added: `OperationFailure` goes from 9 fields to 10,
  `BriosaOperationCapability` from 8 to 10 and `BriosaServerSnapshot` from 8
  to 10, so code that unpacks an exact number of values needs updating.
- Your own subclass of one of those three types that adds fields, or that
  declares a field or property with the name of a field 0.5.1 added, may need
  changes, and pickles of such subclasses written by 0.5.0 are not guaranteed
  to load correctly.
- A subclass of one of those three types can define a read-only property
  named like a field added in 0.5.1. Constructing an instance with the
  inherited initializer raises `AttributeError`.
- Field changes can affect 0.5.0 pickles of `@dataclass(slots=True)`
  subclasses of those three types. Positional restoration can put a subclass
  value into a field added in 0.5.1 and leave a subclass field unset. Reading
  an unset field raises `AttributeError`.
- On 64-bit CPython, `BriosaStartOptions` and its subclasses occupy one
  additional pointer-sized slot.
- On Python 3.10, `get_type_hints(BriosaStartOptions.__init__)["logging"]`
  displays `BriosaLoggingOptions | None`. Version 0.5.0 displayed
  `typing.Optional[BriosaLoggingOptions]`. The two compare equal.
- With an eager task factory and a subclass that permits a nonpositive
  timeout, 0.5.0 could enter the launcher before timing out. Version 0.5.1
  times out before launch.
- Client 0.5.0 can't load a `BriosaServerSnapshot` pickled by 0.5.1, or an
  `OperationFailure` or `BriosaOperationCapability` pickled by 0.5.1 that
  carries a policy denial detail or request options.
