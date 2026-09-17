from __future__ import annotations

from dataclasses import dataclass

from .validation import integer_minor, nonblank


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
    traceability of individual currency units. All lots must already be in one
    currency and the caller supplies verified chronological order. This pure
    function does not persist spend IDs or prevent cross-call double spending.
    """
    nonblank(spend_id, "spend_id")
    integer_minor(amount_minor, "amount_minor", minimum=1)

    seen: set[str] = set()
    available = 0
    for lot in lots:
        nonblank(lot.lot_id, "lot_id")
        nonblank(lot.supporter_id, "supporter_id")
        if lot.lot_id in seen:
            raise ValueError(f"duplicate lot_id: {lot.lot_id}")
        seen.add(lot.lot_id)
        integer_minor(lot.remaining_minor, "remaining_minor")
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
