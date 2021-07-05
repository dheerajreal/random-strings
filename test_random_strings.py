import re
import unittest

from random_strings import get_random_string


class TestRandomStrings(unittest.TestCase):
    def _string_lengths(self, length):
        string = get_random_string(length)
        match = re.fullmatch(r"^[a-zA-Z0-9]+$", string)
        self.assertIsNotNone(match)
        self.assertEqual(len(string), length)

    def test_small_string(self):
        self._string_lengths(12)

    def test_medium_string(self):
        self._string_lengths(32)

    def test_long_string(self):
        self._string_lengths(512)

    def test_invalid_length(self):
        for i in [0, -5, None, "hello", 3.14]:
            with self.assertRaises(ValueError):
                self._string_lengths(i)


if __name__ == "__main__":
    unittest.main()
