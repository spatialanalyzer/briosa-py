"""Reflection on the constructor of ``BriosaStartOptions``, as 0.5.0 code might use it.

``fixtures/options-reflection-0.5.0.json`` holds what ``describe()`` returned
with the published 0.5.0 wheel of this target, once on each Python version
listed, so this module's name and classes must stay as they are. Run it as a
script to print the same description for the installed client.
"""

from __future__ import annotations

import inspect
import json
import sys
import typing
from collections.abc import Callable
from typing import Any

from briosa import BriosaStartOptions


class InheritedStartOptions(BriosaStartOptions):
    """An ordinary subclass that inherits the constructor."""


def _argspec(target: Callable[..., Any]) -> dict[str, str]:
    spec = inspect.getfullargspec(target)
    return {name: repr(getattr(spec, name)) for name in spec._fields}


def _describe(cls: type[Any]) -> dict[str, Any]:
    init = cls.__init__
    return {
        "signature": str(inspect.signature(cls)),
        "signature-init": str(inspect.signature(init)),
        "signature-init-not-followed": str(
            inspect.signature(init, follow_wrapped=False)
        ),
        "getfullargspec": _argspec(cls),
        "getfullargspec-init": _argspec(init),
        "type-hints-init": {
            name: repr(value) for name, value in typing.get_type_hints(init).items()
        },
        "slots": repr(cls.__slots__),
        "dir": sorted(dir(cls())),
        "init": {
            name: repr(getattr(init, name))
            for name in (
                "__name__",
                "__qualname__",
                "__doc__",
                "__module__",
                "__annotations__",
                "__defaults__",
                "__kwdefaults__",
            )
        },
    }


def describe() -> dict[str, Any]:
    return {
        "BriosaStartOptions": _describe(BriosaStartOptions),
        "InheritedStartOptions": _describe(InheritedStartOptions),
    }


if __name__ == "__main__":
    json.dump(
        {"python": sys.version.split()[0], "reflection": describe()},
        sys.stdout,
        indent=1,
    )
