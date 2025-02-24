import random
import string


def random_string(length=10):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))


def generate_user():
    return {
        "email": f"{random_string()}@yandextestov.ruuuuu",
        "password": random_string(),
        "name": random_string(5)
    }



