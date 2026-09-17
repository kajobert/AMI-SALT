import unittest

from salt.runway import project_runway


class RunwayProjectionTests(unittest.TestCase):
    def test_projects_whole_hours(self):
        result = project_runway(
            reserve_minor=10_000,
            hourly_burn_minor=1_500,
            model_version="cost-model-v0.1",
        )
        self.assertEqual(result.projected_hours, 6)

    def test_zero_reserve_is_valid(self):
        result = project_runway(
            reserve_minor=0,
            hourly_burn_minor=100,
            model_version="cost-model-v0.1",
        )
        self.assertEqual(result.projected_hours, 0)

    def test_rejects_nonpositive_burn(self):
        with self.assertRaises(ValueError):
            project_runway(
                reserve_minor=100,
                hourly_burn_minor=0,
                model_version="cost-model-v0.1",
            )

    def test_rejects_negative_reserve(self):
        with self.assertRaises(ValueError):
            project_runway(
                reserve_minor=-1,
                hourly_burn_minor=100,
                model_version="cost-model-v0.1",
            )


if __name__ == "__main__":
    unittest.main()
