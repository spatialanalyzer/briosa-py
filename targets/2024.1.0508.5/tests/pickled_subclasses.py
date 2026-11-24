"""User subclasses of the 0.5.0 dataclasses, as a 0.5.0 application might write.

``fixtures/pickled-0.5.0-subclasses.json`` holds values of these classes as the
published 0.5.0 wheel pickled them, so this module's name and classes must stay
as they are. Each type has an ordinary and a slotted subclass that adds one
field, ``tag``.
"""

from __future__ import annotations

from dataclasses import dataclass

from briosa import (
    BriosaOperationCapability,
    BriosaServerSnapshot,
    BriosaStartOptions,
    OperationFailure,
)


@dataclass(frozen=True)
class OrdinaryStartOptions(BriosaStartOptions):
    tag: str = "untagged"


@dataclass(frozen=True, slots=True)
class SlottedStartOptions(BriosaStartOptions):
    tag: str = "untagged"


@dataclass(frozen=True)
class OrdinaryFailure(OperationFailure):
    tag: str = "untagged"


@dataclass(frozen=True, slots=True)
class SlottedFailure(OperationFailure):
    tag: str = "untagged"


@dataclass(frozen=True)
class OrdinaryCapability(BriosaOperationCapability):
    tag: str = "untagged"


@dataclass(frozen=True, slots=True)
class SlottedCapability(BriosaOperationCapability):
    tag: str = "untagged"


# 0.5.0's last snapshot field has no default, so a subclass field may be required.
@dataclass(frozen=True)
class OrdinarySnapshot(BriosaServerSnapshot):
    tag: str


@dataclass(frozen=True, slots=True)
class SlottedSnapshot(BriosaServerSnapshot):
    tag: str
