import unittest
from task import my_datetime


class TestMyDateTime(unittest.TestCase):
    """Test the function my_datetime import from task.py"""
    def test_epoch_start(self):
        """Test the epoch start is correctly identified."""
        self.assertEqual(my_datetime(0), '01-01-1970')

    def test_arbitrary_date(self):
        """Test the example 123456789 whether convert to correct year"""
        self.assertEqual(my_datetime(123456789), '11-29-1973')

    def test_far_future_date(self):
        """Test the far future date 9876543210 whether convert correctly"""
        self.assertEqual(my_datetime(9876543210), '12-22-2282')


if __name__ == '__main__':
    unittest.main()
