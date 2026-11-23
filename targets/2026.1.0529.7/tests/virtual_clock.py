"""An asyncio event loop on virtual time, for exact startup-budget tests.

Whenever the loop would wait, it jumps to its next timer instead, so a deadline
fires at exactly its scheduled instant and a test can read ``loop.time()`` to
see when it fired. Setting ``loop.now`` inside a coroutine, without yielding,
models time spent while the loop was blocked: a timer that falls due that way
runs only once the running task next yields.
"""

from __future__ import annotations

import asyncio
import selectors
from collections.abc import Awaitable, Callable
from typing import Any, TypeVar

_Result = TypeVar("_Result")


class VirtualClockLoop(asyncio.SelectorEventLoop):
    def __init__(self, now: float = 0.0, *, timer_limit: float | None = None) -> None:
        super().__init__(selectors.SelectSelector())
        self.now = now
        # A loop whose timers have a limited range, as Qt's do under qasync.
        self.timer_limit = timer_limit

    def time(self) -> float:
        return self.now

    def call_at(  # type: ignore[override]
        self, when: float, callback: Callable[..., object], *args: Any, **kwargs: Any
    ) -> asyncio.TimerHandle:
        if self.timer_limit is not None and when - self.now > self.timer_limit:
            raise OverflowError("timer delay out of range")
        return super().call_at(when, callback, *args, **kwargs)

    def armed(self) -> list[float]:
        """The instants of the timers still armed."""
        return sorted(
            handle.when()
            for handle in self._scheduled  # type: ignore[attr-defined]
            if not handle.cancelled()
        )

    def _run_once(self) -> None:
        if not self._ready:  # type: ignore[attr-defined]
            armed = self.armed()
            if armed:
                self.now = max(self.now, armed[0])
        super()._run_once()  # type: ignore[misc]


def run_virtual(
    body: Callable[[VirtualClockLoop], Awaitable[_Result]],
    *,
    now: float = 0.0,
    timer_limit: float | None = None,
) -> _Result:
    loop = VirtualClockLoop(now, timer_limit=timer_limit)
    try:
        return loop.run_until_complete(body(loop))
    finally:
        loop.run_until_complete(loop.shutdown_asyncgens())
        loop.close()
