def get_random_password() -> str:
    import string
    str_ = string.ascii_uppercase + string.ascii_lowercase + string.digits
    from random import sample
    str_ = "".join(sample(str_, 8))

    return str_


print(get_random_password())
