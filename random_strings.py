import secrets
import string


def get_random_string(length: int, lower=True, upper=True, digit=True):
    chars = ""
    if lower:
        chars = chars + string.ascii_lowercase
    if upper:
        chars = chars + string.ascii_uppercase
    if digit:
        chars = chars + string.digits
    return "".join(secrets.choice(chars) for i in range(length))
