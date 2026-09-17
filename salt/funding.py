from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class FundingLot:
    lot_id: str
    supporter_id: str
    remaining_minor: int


@dataclass(frozen=True)
class FundingAllocation:
    spend_id: str
    lot_id: str
    supporter_id: str
    amount_minor: int


def allocate_fifo(
    *,
    spend_id: str,
    amount_minor: int,
    lots: tuple[FundingLot, ...],
) -> tuple[tuple[FundingAllocation, ...], tuple[FundingLot, ...]]:
    """Allocate one spend deterministically across funding lots in FIFO order.

    This is accounting provenance for pooled funds. It does not claim physical
    traceability of individual currency units.
    """
    if not spend_id.strip():
        raise ValueError("spend_id is required")
    if amount_minor <= 0:
        raise ValueError("amount_minor must be > 0")

    seen: set[str] = set()
    available = 0
    for lot in lots:
        if not lot.lot_id.strip():
            raise ValueError("lot_id is required")
        if lot.lot_id in seen:
            raise ValueError(f"duplicate lot_id: {lot.lot_id}")
        seen.add(lot.lot_id)
        if lot.remaining_minor < 0:
            raise ValueError("remaining_minor must be >= 0")
        available += lot.remaining_minor

    if available < amount_minor:
        raise ValueError("insufficient funded balance")

    remaining_spend = amount_minor
    allocations: list[FundingAllocation] = []
    updated: list[FundingLot] = []

    for lot in lots:
        consumed = min(lot.remaining_minor, remaining_spend)
        if consumed:
            allocations.append(
                FundingAllocation(
                    spend_id=spend_id,
                    lot_id=lot.lot_id,
                    supporter_id=lot.supporter_id,
                    amount_minor=consumed,
                )
            )
            remaining_spend -= consumed

        updated.append(
            FundingLot(
                lot_id=lot.lot_id,
                supporter_id=lot.supporter_id,
                remaining_minor=lot.remaining_minor - consumed,
            )
        )

    return tuple(allocations), tuple(updated)
