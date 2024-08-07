import unittest
import random
from datetime import datetime, timedelta, timezone
from task import my_datetime, conv_num, conv_endian


class TestConvNum(unittest.TestCase):
    """Test the conv_num function from task.py"""

    def test_wrong_type1(self):
        """Test if that a non-string argument
        returns None"""
        self.assertEqual(conv_num(12366), None)

    def test_wrong_type2(self):
        """Test if that a non-string argument
        returns None"""
        self.assertEqual(conv_num([12366]), None)

    def test_empty_string(self):
        """Test if that a non-string argument
        returns None"""
        self.assertEqual(conv_num(''), None)

    def test_int(self):
        """Test if a string containing int
        returns a int type"""
        self.assertEqual(conv_num("1234560"), 1234560)

    def test_negative_int(self):
        """Test if a string containing int
        returns a int type"""
        self.assertEqual(conv_num("-1234560"), -1234560)

    def test_bad_int(self):
        """Test if a string containing a bad int
        returns None"""
        self.assertEqual(conv_num("-12345A0"), None)

    def test_float1(self):
        """Test if a string containing float
        returns a float type"""
        self.assertEqual(conv_num("123.4589"), 123.4589)

    def test_float2(self):
        """Test if a string containing float
        returns a float type"""
        self.assertEqual(conv_num("1.234589"), 1.234589)

    def test_float3(self):
        """Test if a string containing negative float
        returns a negative float type"""
        self.assertEqual(conv_num("-1234589."), -1234589.0)

    def test_float4(self):
        """Test if a string containing negative float
        returns a float type"""
        self.assertEqual(conv_num("-.1234589"), -0.1234589)

    def test_float5(self):
        """Test if a string containing float
        returns a float type"""
        self.assertEqual(conv_num(".45"), 0.45)

    def test_double_decimal(self):
        """Test if a string containing more than one
        decimal point returns None"""
        self.assertEqual(conv_num("12.3.45"), None)

    def test_hex1(self):
        """Test if a string containing a hexadecimal
        number returns an int"""
        self.assertEqual(conv_num("0xad4"), 2772)

    def test_hex2(self):
        """Test if a string containing a hexadecimal
        number returns an int"""
        self.assertEqual(conv_num("0xAD4"), 2772)

    def test_negative_hex(self):
        """Test if a string containing a hexadecimal
        number returns an int"""
        self.assertEqual(conv_num("-0xAD4"), -2772)

    def test_bad_hex(self):
        """Test if a string containing a bad hexadecimal
        number returns an None"""
        self.assertEqual(conv_num("0xAZ4"), None)

    def test_bad_hex2(self):
        """Test if a string containing a bad hexadecimal
        number returns an None"""
        self.assertEqual(conv_num("-0xAZ4"), None)

    def test_bad_hex3(self):
        """Test if a string containing a bad hexadecimal
        number returns an None"""
        self.assertEqual(conv_num("-0xAZ.4"), None)

    def test_bad_input1(self):
        """Test if a string containing a bad input '.'
        returns an None"""
        self.assertEqual(conv_num("."), None)

    def test_bad_input2(self):
        """Test if a string containing a bad input
        returns an None"""
        self.assertEqual(conv_num("123$45"), None)

    def test_bad_input3(self):
        """Test if a string containing a bad input
        returns an None"""
        self.assertEqual(conv_num("123-45"), None)

    def test_bad_input4(self):
        """Test if a string containing a bad input
        returns an None"""
        self.assertEqual(conv_num("12 3 45"), None)


class TestMyDateTime(unittest.TestCase):
    """Test the function my_datetime import from task.py"""

    def test_epoch_start(self):
        """Test the epoch start is correctly identified."""
        self.assertEqual(my_datetime(0), '01-01-1970')

    def test_arbitrary_date(self):
        """Test the example 123456789 whether convert to correct year"""
        self.assertEqual(my_datetime(123456789), '11-29-1973')

    def test_far_future_date(self):
        """Test the example whether convert to far future date correctly"""
        self.assertEqual(my_datetime(9876543210), '12-22-2282')

    def test_leap_year_date(self):
        """Test whether it convert to leap year correctly"""
        self.assertEqual(my_datetime(201653971200), '02-29-8360')

    def test_special_leap_year(self):
        """Test whether it convert to special leap year correctly"""
        self.assertEqual(my_datetime(946684800), '01-01-2000')

    def test_edge_year(self):
        """Test whether it convert to an edge year correctly"""
        self.assertEqual(my_datetime(253402217200), "12-31-9999")


class TestRandomMyDatetime(unittest.TestCase):
    """Random number of seconds that potentially could span up to year
    9999 Calculate the total number of seconds from epoch to 12-31-9999"""

    def test_extended_random_dates(self):
        """Generate 1000 random test cases"""
        for _ in range(1000):
            end_date = datetime(9999, 12, 31, 23, 59, 59, tzinfo=timezone.utc)
            epoch_start = datetime(1970, 1, 1, tzinfo=timezone.utc)
            max_seconds = int((end_date - epoch_start).total_seconds())

            num_sec = random.randint(0, max_seconds)

            # Calculate expected date using datetime
            expected_date = epoch_start + timedelta(seconds=num_sec)
            expected_date_str = expected_date.strftime('%m-%d-%Y')

            # Get the result from your function
            result = my_datetime(num_sec)

            # Check if the result matches the expected value
            self.assertEqual(result, expected_date_str)


class TestConvEndian(unittest.TestCase):
    """Test the conv_endian function from task.py"""

    def test1(self):
        """Test for module example with valid 'big' endian"""
        expected = '0E 91 A2'
        result = conv_endian(954786, 'big')
        self.assertEqual(result, expected)

    def test2(self):
        """Test for module example with no endian specified"""
        expected = '0E 91 A2'
        result = conv_endian(954786)
        self.assertEqual(result, expected)

    def test3(self):
        """Test for module example with negative integer and no endian specified"""
        expected = '-0E 91 A2'
        result = conv_endian(-954786)
        self.assertEqual(result, expected)

    def test4(self):
        """Test for module example with valid 'little' endian"""
        expected = 'A2 91 0E'
        result = conv_endian(954786, 'little')
        self.assertEqual(result, expected)

    def test5(self):
        """Test for module example with negative value and valid 'little' endian"""
        expected = '-A2 91 0E'
        result = conv_endian(-954786, 'little')
        self.assertEqual(result, expected)

    def test6(self):
        """Test for module example with negative value and invalid endian"""
        expected = None
        result = conv_endian(-954786, 'small')
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
