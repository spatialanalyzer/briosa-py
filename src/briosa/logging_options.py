"""Startup-only server logging controls; no client-side log processing."""

from __future__ import annotations

import re
from collections.abc import Mapping
from dataclasses import dataclass, field
from enum import Enum
from pathlib import PureWindowsPath
from types import MappingProxyType


class BriosaLogLevel(str, Enum):
    TRACE = "Trace"
    DEBUG = "Debug"
    INFORMATION = "Information"
    WARNING = "Warning"
    ERROR = "Error"
    CRITICAL = "Critical"
    NONE = "None"


@dataclass(frozen=True, slots=True)
class BriosaLoggingOptions:
    minimum_level: BriosaLogLevel | None = None
    category_levels: Mapping[str, BriosaLogLevel] = field(default_factory=dict)
    console_enabled: bool | None = None
    file_enabled: bool | None = None
    file_directory: str | None = None
    max_file_size_mib: int | None = None
    retained_file_count: int | None = None
    max_age_days: int | None = None
    max_total_size_mib: int | None = None

    def __post_init__(self) -> None:
        object.__setattr__(
            self, "category_levels", MappingProxyType(dict(self.category_levels))
        )
        self.to_arguments()

    def to_arguments(self) -> list[str]:
        """Return validated argument-list entries, never shell command text."""
        if self.minimum_level is not None and not isinstance(
            self.minimum_level, BriosaLogLevel
        ):
            raise ValueError("Invalid server logging options")
        for category, level in self.category_levels.items():
            if not re.fullmatch(r"[A-Za-z0-9_.]{1,256}", category) or not isinstance(
                level, BriosaLogLevel
            ):
                raise ValueError("Invalid server logging options")
        for value in (self.console_enabled, self.file_enabled):
            if value is not None and type(value) is not bool:
                raise ValueError("Invalid server logging options")
        if self.file_directory is not None and (
            not PureWindowsPath(self.file_directory).is_absolute()
            or any(ord(c) < 32 for c in self.file_directory)
        ):
            raise ValueError("Invalid server logging options")
        for number, maximum in (
            (self.max_file_size_mib, 1024),
            (self.retained_file_count, 1000),
            (self.max_age_days, 365),
            (self.max_total_size_mib, 10240),
        ):
            if number is not None and (
                type(number) is not int or not 1 <= number <= maximum
            ):
                raise ValueError("Invalid server logging options")
        if (
            self.max_total_size_mib is not None
            and self.max_file_size_mib is not None
            and self.max_total_size_mib < self.max_file_size_mib
        ):
            raise ValueError("Invalid server logging options")
        values: dict[str, str | bool | int | None] = {
            "Logging:LogLevel:Default": (
                self.minimum_level.value if self.minimum_level is not None else None
            ),
            **{
                f"Logging:LogLevel:{category}": level.value
                for category, level in self.category_levels.items()
            },
            "Briosa:Logging:ConsoleEnabled": self.console_enabled,
            "Briosa:Logging:File:Enabled": self.file_enabled,
            "Briosa:Logging:File:Directory": self.file_directory,
            "Briosa:Logging:File:MaxFileSizeMiB": self.max_file_size_mib,
            "Briosa:Logging:File:RetainedFileCount": self.retained_file_count,
            "Briosa:Logging:File:MaxAgeDays": self.max_age_days,
            "Briosa:Logging:File:MaxTotalSizeMiB": self.max_total_size_mib,
        }
        return [
            f"--{key}={value}" for key, value in values.items() if value is not None
        ]
