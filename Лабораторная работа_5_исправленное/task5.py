from string import ascii_uppercase, ascii_lowercase, digits
from random import sample


def get_random_password(n) -> str:

    str_ = ascii_uppercase + ascii_lowercase + digits
    str_ = "".join(sample(str_, n))

    return str_


print(get_random_password(8))
