# password_gen.py

import random
import string

def generate_password(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

print("Password Generator")

try:
    length = int(input("Enter password length (default 12): ") or 12)
except ValueError:
    length = 12

print("Generated Password:", generate_password(length))
