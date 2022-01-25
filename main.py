import random

num_password = int(input("Input your amount of passwords: "))
password_length = int(input("Input your password lengths: "))
chars = 'abcdefghjklmnopqrstuvwxyzABCDEFGHJKLMNOPQRSTUVWXYZ!@#$%^&*()0123456789'

for x in range(num_password):
    passwords = ''
    for z in range(password_length):
        passwords += random.choice(chars)
    print(f"\nHere are you passwords: {passwords}")
