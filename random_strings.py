import secrets
import string


def get_random_string(
    length: int,
    lower: bool = True,
    upper: bool = True,
    digit: bool = True
) -> str:
    """Generate random strings suitable for cryptographic use.

    Args:
        length (int, required):
            Length of string.
        lower (bool, optional):
            Should lowercase characters(a-z) be included. Defaults to True.
        upper (bool, optional):
            Should uppercase characters(A-Z) be included. Defaults to True.
        digit (bool, optional):
            Should digit characters(0-9) be included. Defaults to True.

    Raises:
        ValueError:
            When integer less than zero or non-integer value for length is given.

    Returns:
        str: Cryptographically-secure string of given length.
    """
    if not (length and isinstance(length, int) and length > 0):
        raise ValueError("length must be an integer greater than zero")
    chars = ""
    if lower:
        chars = chars + string.ascii_lowercase
    if upper:
        chars = chars + string.ascii_uppercase
    if digit:
        chars = chars + string.digits
    return "".join(secrets.choice(chars) for i in range(length))
