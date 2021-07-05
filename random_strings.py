import secrets
import string


def get_random_string(
    length: int,
    lower: bool = True,
    upper: bool = True,
    digit: bool = True
) -> str:
    if not isinstance(length, int):
        raise ValueError("length must be an integer")
    if not length > 0:
        raise ValueError("length must be greater than zero")
    chars = ""
    if lower:
        chars = chars + string.ascii_lowercase
    if upper:
        chars = chars + string.ascii_uppercase
    if digit:
        chars = chars + string.digits
    return "".join(secrets.choice(chars) for i in range(length))
