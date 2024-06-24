import random

chars = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
password = ""

length = int(input('How long will the password be? '))

for char in range(length):
    password += random.choice(chars)

print(password)