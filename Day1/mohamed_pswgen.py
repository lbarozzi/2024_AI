
import string
import secrets
import random

password = secrets.token_urlsafe(32)
from random import sample, choice

chars = string.ascii_letters + string.digits + string.punctuation
length = 12

random_password1 = ''.join (sample(chars, length))
random_password2 = ''.join (choice(chars) for i in range(length))

print(f"Random Password (using sample): {random_password1}")
print(f"Random Password (using choice): {random_password2}")
