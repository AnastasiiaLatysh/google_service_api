import string
from random import choices


def get_random_string_with_digits(string_length=10):
    """
    Generate random string with ASCII letters in lower case mode
    :param string_length: (int) length of string which should be generated
    :return: (str)
    """
    return ''.join(choices(string.ascii_lowercase + string.digits, k=string_length))
