import datetime
import unittest

from unittest.mock import patch

import mocks

from dott.runner import HourRunner


class Test_Calc_Next_Run(unittest.TestCase):
    @patch("dott.runner.HourRunner.get_now", side_effect=mocks.mock_get_now, autospec=True)
    def test_expected_equal(self, mock_now):
        """Expected result is equal to result."""
        expecting = datetime.datetime(2019, 7, 15, 16, 0, 0)
        self.assertEqual(expecting, HourRunner._calc_next_run([1]))
    
    @patch("dott.runner.HourRunner.get_now", side_effect=mocks.mock_get_now, autospec=True)
    def test_expected_not_equal(self, mock_now):
        """Expected result is not equal to result.""" 
        expecting = datetime.datetime(2019, 7, 15, 17, 0, 0)
        self.assertNotEqual(expecting, HourRunner._calc_next_run([1]))


if __name__ == "__main__":
    unittest.main()
