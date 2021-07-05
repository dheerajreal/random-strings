import re
import unittest

from random_strings import get_random_string


class TestRandomStrings(unittest.TestCase):
    UPPER_LOWER_DIGIT_REGEX = r"^[A-Za-z0-9]+$"
    NOUPPER_LOWER_DIGIT_REGEX = r"^[a-z0-9]+$"
    UPPER_NOLOWER_DIGIT_REGEX = r"^[A-Z0-9]+$"
    UPPER_LOWER_NODIGIT_REGEX = r"^[A-Za-z]+$"
    NOUPPER_NOLOWER_DIGIT_REGEX = r"^[0-9]+$"
    NOUPPER_LOWER_NODIGIT_REGEX = r"^[a-z]+$"
    UPPER_NOLOWER_NODIGIT_REGEX = r"^[A-Z]+$"
    valid_lengths = [8, 16, 32, 64, 512, 2048, True]  # True returns length 1
    invalid_lengths = [0, -5, "hello", 3.14, {}, None, False]

    def _string_lengths(self, length, *args, regex="", **kwargs):
        string = get_random_string(length, *args, **kwargs)
        match = re.fullmatch(regex, string)
        self.assertIsNotNone(match)
        self.assertEqual(len(string), length)

    def _invalid_string_lengths(self, length, *args, regex="", **kwargs):
        with self.assertRaises(ValueError):
            self._string_lengths(length, *args, regex=regex, **kwargs)

    def test_valid_string_lengths(self):
        for length in self.valid_lengths:
            self._string_lengths(length, regex=self.UPPER_LOWER_DIGIT_REGEX)

    def test_invalid_string_lengths(self):
        for length in self.invalid_lengths:
            self._invalid_string_lengths(
                length, regex=self.UPPER_LOWER_DIGIT_REGEX)

    def test_upper_false(self):
        for length in self.valid_lengths:
            self._string_lengths(
                length, regex=self.NOUPPER_LOWER_DIGIT_REGEX, upper=False)

    def test_lower_false(self):
        for length in self.valid_lengths:
            self._string_lengths(
                length, regex=self.UPPER_NOLOWER_DIGIT_REGEX, lower=False)

    def test_digit_false(self):
        for length in self.valid_lengths:
            self._string_lengths(
                length, regex=self.UPPER_LOWER_NODIGIT_REGEX, digit=False)

    def test_upper_lower_false(self):
        for length in self.valid_lengths:
            self._string_lengths(
                length, regex=self.NOUPPER_NOLOWER_DIGIT_REGEX, upper=False, lower=False)

    def test_upper_digit_false(self):
        for length in self.valid_lengths:
            self._string_lengths(
                length, regex=self.NOUPPER_LOWER_NODIGIT_REGEX, upper=False, digit=False)

    def test_lower_digit_false(self):
        for length in self.valid_lengths:
            self._string_lengths(
                length, regex=self.UPPER_NOLOWER_NODIGIT_REGEX, lower=False, digit=False)


if __name__ == "__main__":
    unittest.main()
