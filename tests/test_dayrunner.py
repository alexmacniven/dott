import datetime
import unittest

from unittest.mock import patch

import mocks

from dott.runner import DayRunner


class Test_Calc_Next_Run(unittest.TestCase):

    @patch("dott.runner.DayRunner.get_now", side_effect=mocks.mock_get_now, autospec=True)
    def test_expected_equal(self, mock_now):
        """Expected result is equal to result."""
        expecting = datetime.datetime(2019, 7, 15, 20, 0)
        self.assertEqual(expecting, DayRunner._calc_next_run(["20:00"]))

    @patch("dott.runner.DayRunner.get_now", side_effect=mocks.mock_get_now, autospec=True)
    def test_expected_not_equal(self, mock_now):
        """Expected result is not equal to result."""
        expecting = datetime.datetime(2019, 7, 15, 21, 0)
        self.assertNotEqual(expecting, DayRunner._calc_next_run(["20:00"]))


if __name__ == "__main__":
    unittest.main()
