from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal, ROUND_DOWN


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
    if reserve_minor < 0:
        raise ValueError("reserve_minor must be >= 0")
    if hourly_burn_minor <= 0:
        raise ValueError("hourly_burn_minor must be > 0")
    if not model_version.strip():
        raise ValueError("model_version is required")

    hours = int(
        (Decimal(reserve_minor) / Decimal(hourly_burn_minor)).quantize(
            Decimal("1"), rounding=ROUND_DOWN
        )
    )
    return RunwayProjection(
        reserve_minor=reserve_minor,
        hourly_burn_minor=hourly_burn_minor,
        projected_hours=hours,
        model_version=model_version,
    )
