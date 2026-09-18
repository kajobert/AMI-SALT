import unittest

from salt.funding import FundingLot, allocate_fifo
from salt.runway import project_runway


class NumericContractTests(unittest.TestCase):
    def test_rejects_noninteger_spend(self):
        for value in (True, False, 0.5, float('nan'), float('inf'), '1', None):
            with self.subTest(value=value), self.assertRaises(ValueError):
                allocate_fifo(spend_id='s', amount_minor=value,
                              lots=(FundingLot('a', 'alice', 100),))

    def test_rejects_noninteger_lot_balance(self):
        for value in (True, 1.5, float('nan'), '1', None):
            with self.subTest(value=value), self.assertRaises(ValueError):
                allocate_fifo(spend_id='s', amount_minor=1,
                              lots=(FundingLot('a', 'alice', value),))

    def test_rejects_missing_supporter(self):
        for value in ('', ' ', None, 3):
            with self.subTest(value=value), self.assertRaises(ValueError):
                allocate_fifo(spend_id='s', amount_minor=1,
                              lots=(FundingLot('a', value, 100),))

    def test_rejects_invalid_identifiers(self):
        for value in ('', ' ', None, 3):
            with self.subTest(value=value), self.assertRaises(ValueError):
                allocate_fifo(spend_id=value, amount_minor=1,
                              lots=(FundingLot('a', 'alice', 100),))

    def test_rejects_noninteger_runway(self):
        for key in ('reserve_minor', 'hourly_burn_minor'):
            for value in (True, 1.5, float('nan'), '1', None):
                arguments = dict(reserve_minor=100, hourly_burn_minor=1, model_version='v1')
                arguments[key] = value
                with self.subTest(key=key, value=value), self.assertRaises(ValueError):
                    project_runway(**arguments)

    def test_large_integer_runway_is_exact(self):
        reserve = 10**80 + 7
        result = project_runway(reserve_minor=reserve, hourly_burn_minor=3, model_version='v1')
        self.assertEqual(result.projected_hours, reserve // 3)

    def test_invalid_model_version(self):
        for value in ('', ' ', None, 3):
            with self.subTest(value=value), self.assertRaises(ValueError):
                project_runway(reserve_minor=1, hourly_burn_minor=1, model_version=value)

    def test_allocation_conserves_balance_and_does_not_mutate_inputs(self):
        for amount in range(1, 18):
            lots = (FundingLot('a', 'alice', 7), FundingLot('b', 'bob', 10))
            allocations, updated = allocate_fifo(spend_id='s', amount_minor=amount, lots=lots)
            self.assertEqual(sum(x.amount_minor for x in allocations), amount)
            self.assertEqual(sum(x.remaining_minor for x in updated) + amount, 17)
            self.assertEqual([x.remaining_minor for x in lots], [7, 10])
            self.assertTrue(all(x.remaining_minor >= 0 for x in updated))

    def test_allocation_reproducibility(self):
        kwargs = dict(spend_id='s', amount_minor=120,
                      lots=(FundingLot('a', 'alice', 100), FundingLot('b', 'bob', 100)))
        self.assertEqual(allocate_fifo(**kwargs), allocate_fifo(**kwargs))

    def test_empty_and_zero_balance_rejected(self):
        for lots in ((), (FundingLot('a', 'alice', 0),)):
            with self.assertRaises(ValueError):
                allocate_fifo(spend_id='s', amount_minor=1, lots=lots)
