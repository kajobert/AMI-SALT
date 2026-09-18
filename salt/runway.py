from __future__ import annotations

from dataclasses import dataclass
from .validation import integer_minor, nonblank


@dataclass(frozen=True)
class RunwayProjection:
    reserve_minor: int
    hourly_burn_minor: int
    projected_hours: int
    model_version: str


def project_runway(*, reserve_minor: int, hourly_burn_minor: int, model_version: str) -> RunwayProjection:
    """Project whole funded hours using integer minor currency units.

    This is an accounting estimate, not SALT issuance and not a financial promise.
    """
    integer_minor(reserve_minor, "reserve_minor")
    integer_minor(hourly_burn_minor, "hourly_burn_minor", minimum=1)
    nonblank(model_version, "model_version")
    hours = reserve_minor // hourly_burn_minor
    return RunwayProjection(
        reserve_minor=reserve_minor,
        hourly_burn_minor=hourly_burn_minor,
        projected_hours=hours,
        model_version=model_version,
    )
