from random import choice
from string import punctuation as symbols
from string import ascii_letters as letters
from string import digits as number


class PasswordGenerator():
    """
    Generate a strong password.
    """
    def create_password(self, digit=8):
        digits = int(digit)
        values = letters + number + symbols
        Password = ""

        for i in range(digits):
            Password += choice(values)
        return Password


Password = PasswordGenerator().create_password(20)

print("-"*100)
print("Password: ", Password)
print("-"*100)
