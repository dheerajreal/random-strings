import secrets
import string
from uuid import uuid4

__all__ = ["get_random_string", "get_random_hex", "get_random_uuid"]


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


_DEFAULT_ENTROPY = 64


def get_random_hex(nbytes: int = None) -> str:
    """Generate random hexadecimal string suitable for cryptographic use.

    Args:
        nbytes (int, optional):
            Number of bytes. Two characters generated for each byte.
            A suitable default will we used if not given.

    Returns:
        str: Cryptographically-secure hexadecimal string for given number of bytes of randomness.
    """
    if not nbytes:
        nbytes = _DEFAULT_ENTROPY  # Default
    return secrets.token_hex(nbytes=nbytes)


def get_random_uuid(dashes: bool = True) -> str:
    """Generate random uuid string suitable for cryptographic use.

    Args:
        dashes (bool, optional):
            should dashes be included in the generated string(uuid). Defaults to True.

    Returns:
        str: String representation of randomly generated uuid
    """
    if not dashes:
        return uuid4().hex
    return str(uuid4())
