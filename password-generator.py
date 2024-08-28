import string
import random

def generate_password(length):
    all_chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

print(generate_password(10))