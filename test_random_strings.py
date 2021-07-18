import re
import unittest

from random_strings import random_hex, random_string, random_uuid, _DEFAULT_ENTROPY


class TestRandomStrings(unittest.TestCase):
    UPPER_LOWER_DIGIT_REGEX = r"^[A-Za-z0-9]+$"
    NOUPPER_LOWER_DIGIT_REGEX = r"^[a-z0-9]+$"
    UPPER_NOLOWER_DIGIT_REGEX = r"^[A-Z0-9]+$"
    UPPER_LOWER_NODIGIT_REGEX = r"^[A-Za-z]+$"
    NOUPPER_NOLOWER_DIGIT_REGEX = r"^[0-9]+$"
    NOUPPER_LOWER_NODIGIT_REGEX = r"^[a-z]+$"
    UPPER_NOLOWER_NODIGIT_REGEX = r"^[A-Z]+$"
    valid_lengths = [8, 16, 32, 64, 512, 2048, True]  # True returns length 1
    invalid_lengths = [0, -5, "hello", 3.14, {}, None, False, "", "  "]

    def _string_lengths(self, length, *args, regex="", **kwargs):
        string = random_string(length, *args, **kwargs)
        match = re.fullmatch(regex, string)
        self.assertIsNotNone(match)
        self.assertEqual(len(string), length)

    def _invalid_string_lengths(self, length, *args, regex="", **kwargs):
        with self.assertRaises(ValueError):
            self._string_lengths(length, *args, regex=regex, **kwargs)

    def test_valid_string_lengths(self):
        for length in self.valid_lengths:
            self._string_lengths(
                length,
                regex=self.UPPER_LOWER_DIGIT_REGEX
            )

    def test_invalid_string_lengths(self):
        for length in self.invalid_lengths:
            self._invalid_string_lengths(
                length,
                regex=self.UPPER_LOWER_DIGIT_REGEX
            )

    def test_upper_false(self):
        for length in self.valid_lengths:
            self._string_lengths(
                length,
                regex=self.NOUPPER_LOWER_DIGIT_REGEX,
                upper=False
            )

    def test_lower_false(self):
        for length in self.valid_lengths:
            self._string_lengths(
                length,
                regex=self.UPPER_NOLOWER_DIGIT_REGEX,
                lower=False
            )

    def test_digit_false(self):
        for length in self.valid_lengths:
            self._string_lengths(
                length,
                regex=self.UPPER_LOWER_NODIGIT_REGEX,
                digit=False
            )

    def test_upper_lower_false(self):
        for length in self.valid_lengths:
            self._string_lengths(
                length,
                regex=self.NOUPPER_NOLOWER_DIGIT_REGEX,
                upper=False,
                lower=False
            )

    def test_upper_digit_false(self):
        for length in self.valid_lengths:
            self._string_lengths(
                length,
                regex=self.NOUPPER_LOWER_NODIGIT_REGEX,
                upper=False,
                digit=False
            )

    def test_lower_digit_false(self):
        for length in self.valid_lengths:
            self._string_lengths(
                length,
                regex=self.UPPER_NOLOWER_NODIGIT_REGEX,
                lower=False,
                digit=False
            )

    def test_upper_lower_digit_false(self):
        for length in self.valid_lengths:
            with self.assertRaises(ValueError):
                random_string(
                    length,
                    upper=False,
                    lower=False,
                    digit=False
                )

    def test_custom_character_string(self):
        for length in self.valid_lengths:
            self._string_lengths(
                length,
                regex=r"^\S+$",
                character_string="#$^%&@*()[]"
            )
            string = random_string(
                length,
                character_string="#$^%&@*()[]"
            )
            self.assertIsNone(re.fullmatch(
                self.UPPER_LOWER_DIGIT_REGEX, string))
            string = random_string(
                length,
                character_string="ABCD"
            )
            self.assertIsNotNone(re.fullmatch(r"^[ABCD]+$", string))


class TestRandomHexAndUUID(unittest.TestCase):
    HEX_REGEX = r"^[0-9a-f]+$"
    UUID_REGEX_DASH = r"^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$"
    UUID_REGEX_NODASH = r"^[0-9a-f]{32}$"

    def test_random_hex(self):
        for bytes_len in [False, None, 1, 3, 5, 8, 14, 25, 100, 2500]:
            generated_hex = random_hex(nbytes=bytes_len)
            match = re.fullmatch(self.HEX_REGEX, generated_hex)
            if not bytes_len:
                bytes_len = _DEFAULT_ENTROPY
            self.assertIsNotNone(match)
            self.assertEqual(len(generated_hex), bytes_len * 2)

    def test_random_uuid(self):
        generated_uuid = random_uuid()
        match = re.fullmatch(self.UUID_REGEX_DASH, generated_uuid)
        self.assertIsNotNone(match)

    def test_random_uuid_nodash(self):
        generated_uuid = random_uuid(dashes=False)
        match = re.fullmatch(self.UUID_REGEX_NODASH, generated_uuid)
        self.assertIsNotNone(match)


if __name__ == "__main__":
    print("running tests")
    unittest.main()
