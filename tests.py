import unittest
from task import conv_num


class TestCase(unittest.TestCase):

    def test1(self):
        self.assertTrue(True)

    def test_no_input(self):
        """Test checks to see if no input is accepted"""

        self.assertEqual(conv_num(''), None)

    def test_only_space(self):
        """Test checks to see if a space is accepted"""

        self.assertEqual(conv_num(' '), None)

    def test_space_in_front(self):
        """Test checks to see a space in front is accepted"""

        self.assertEqual(conv_num(' 12345'), None)

    def test_space_in_middle(self):
        """Test checks to see if a space in the middle is accepted"""

        self.assertEqual(conv_num('0x AD4'), None)

    def test_space_at_back(self):
        """Test checks to see if a space at the back is accepted"""

        self.assertEqual(conv_num('12345 '), None)

    def test_multiple_decimals(self):
        """Test checks to see if multiple decimal points are accepted"""

        self.assertEqual(conv_num('12.3.45'), None)

    def test_hex_and_decimal_point(self):
        """Test checks to see if mixed format with hex and decimal points are accepted"""

        self.assertEqual(conv_num('0xFF.02'), None)

    def test_mulitple_negative_signs(self):
        """Test checks to see if multiple negative signs are accepted"""

        self.assertEqual(conv_num('-0xAD4-'), None)

    def test_no_leading_zero(self):
        """Test checks to see if a decimal without a zero accepted"""

        self.assertEqual(conv_num('.45'), 0.45)

    def test_no_trailing_zero(self):
        """Test checks to see if decimals without a trailing zero are returned properly"""

        self.assertEqual(conv_num('123.'), 123.0)

    def test_decimal_with_letter(self):
        """Test checks to see if decimals with letters are accepted"""

        self.assertEqual(conv_num('12345A'), None)

    def test_hex_char_out_of_range(self):
        """Test checks to see if non hex characters are accepted"""

        self.assertEqual(conv_num('0xAg4'), None)

    def test_hex_without_zero(self):
        """Test checks to see if hex entries without the zero are accepted"""

        self.assertEqual(conv_num('X124'), None)


if __name__ == '__main__':
    unittest.main()
