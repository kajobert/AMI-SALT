import unittest

from salt.funding import FundingLot, allocate_fifo


class FundingAllocationTests(unittest.TestCase):
    def test_fifo_allocation_preserves_supporter_provenance(self):
        lots = (
            FundingLot("lot-a", "alice", 100),
            FundingLot("lot-b", "bob", 100),
        )

        allocations, updated = allocate_fifo(
            spend_id="spend-1",
            amount_minor=150,
            lots=lots,
        )

        self.assertEqual(
            [(a.lot_id, a.supporter_id, a.amount_minor) for a in allocations],
            [("lot-a", "alice", 100), ("lot-b", "bob", 50)],
        )
        self.assertEqual([lot.remaining_minor for lot in updated], [0, 50])

    def test_insufficient_balance_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "insufficient funded balance"):
            allocate_fifo(
                spend_id="spend-2",
                amount_minor=101,
                lots=(FundingLot("lot-a", "alice", 100),),
            )

    def test_duplicate_lot_ids_are_rejected(self):
        with self.assertRaisesRegex(ValueError, "duplicate lot_id"):
            allocate_fifo(
                spend_id="spend-3",
                amount_minor=1,
                lots=(
                    FundingLot("same", "alice", 1),
                    FundingLot("same", "bob", 1),
                ),
            )


if __name__ == "__main__":
    unittest.main()
