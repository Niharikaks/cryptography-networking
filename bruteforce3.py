import itertools
import string

def brute_force_password(password, max_length=4):
 characters = string.ascii_letters + string.digits
 for length in range(1, max_length + 1):
     for guess in itertools.product(characters, repeat=length):
         guess = ''.join(guess)
         if guess == password:
             return f"Password '{password}' cracked in {length} tries!"

password = "abc1"
print(brute_force_password(password))