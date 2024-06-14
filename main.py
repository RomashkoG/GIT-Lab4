<<<<<<< Updated upstream
from utils import factorial, is_prime

if __name__ == "__main__":
    number = 5
    print(f"Факторіал числа {number} = {factorial(number)}")
=======
from utils import factorial, is_prime, is_power_of_five, is_power_of_two

if __name__ == "__main__":
    number = 5
    print(f"Факторіал числа {number} = {factorial(number)}")

    print(f"Число {number} {'є' if is_power_of_five(number) else 'не є'} степенем 5")
    print(f"Число {number} {'є' if is_power_of_two(number) else 'не є'} степенем 5")
>>>>>>> Stashed changes
