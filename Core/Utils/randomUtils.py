import random
import string


class RandomUtils:

    __aqa_prefix = "autoqa_"
    __email_suffix = "@mailinator.com"

    @classmethod
    def generate_random_string(cls, length) -> str:
        return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))

    @classmethod
    def generate_random_numbers(cls, length) -> str:
        return ''.join(random.choice(string.digits) for _ in range(length))

    @classmethod
    def generate_random_string_with_digits(cls, length) -> str:
        return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(length))

    @classmethod
    def generate_random_password(cls) -> str:
        return "RSA" + ''.join(random.choice(string.ascii_lowercase + string.digits + string.ascii_uppercase)
                               for _ in range(9)) + ")@!"

    @classmethod
    def generate_random_aqa_name(cls) -> str:
        return cls.__aqa_prefix + ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(5))

    @classmethod
    def generate_random_email(cls) -> str:
        return cls.__aqa_prefix + ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(6)) \
            + cls.__email_suffix
