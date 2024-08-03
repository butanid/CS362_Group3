import unittest
from task import conv_num


class TestConvNum(unittest.TestCase):

    def test_ints(self):
        '''Test if a string containing ints
        returns a int type'''
        self.assertEqual(conv_num("1234560"), 1234560)

    def test_float(self):
        """Test if a string containing floats
        returns a float type"""
        self.assertEqual(conv_num("12345.89"), 12345.89)

    def test_negative(self):
        """Test if a string containing negative float
        returns a negative float"""
        self.assertEqual(conv_num("-123.45"), -123.45)


if __name__ == '__main__':
    unittest.main()
