import random
import string

password_length = int(input("How many characters you want in your password? "))
def generate(len=password_length):
    passw = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choice(passw) for i in range(len))

password = generate(password_length)
print("Your password is ", password)
