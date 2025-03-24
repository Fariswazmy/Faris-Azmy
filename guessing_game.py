import random

def request_user_name():
    user_name = input ("Please enter your name here: ")
    return user_name


def random_digit():
    upper_range = int(input("Set the maximum value for the range: "))
    lower_range = int(input("Set the minimum value for the range: "))
    return random.randint(lower_range, upper_range)


print(f"{request_user_name()}, your random number is: {random_digit()}")
