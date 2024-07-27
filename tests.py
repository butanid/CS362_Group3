import unittest
from task import my_datetime


class TestCase(unittest.TestCase):

    def test1(self):
        self.assertTrue(True)


class TestMyDateTime(unittest.TestCase):
    """Test the function my_datetime import from task.py"""
    def test_epoch_start(self):
        """Test the epoch start is correctly identified."""
        expected_date = '01-01-1970'
        result = my_datetime(0)
        self.assertEqual(result, expected_date)



if __name__ == '__main__':
    unittest.main()
