#Q17
import random
import string

def generate_password():
    chars = string.ascii_letters + string.digits
    password = ''.join(random.choice(chars) for _ in range(8))
    return password

print("Generated password:", generate_password())