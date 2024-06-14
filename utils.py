def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_power_of_five(num):
    if num < 1:
        return False
    while num % 5 == 0:
        num /= 5
    return num == 1

def is_power_of_two(num):
    if num < 1:
        return False
    while num % 2 == 0:
        num /= 2
    return num == 1
