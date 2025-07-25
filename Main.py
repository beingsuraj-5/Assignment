
#Author: Suraj



def is_prime(number: int) -> bool:
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1): 
        if number % i == 0: 
            return False
    return True

def get_previous_prime(number: int) -> int:
    for i in range(number - 1, 1, -1): 
        if is_prime(i): 
            return i
    return None

def get_next_prime(number: int) -> int:
    i = number + 1
    while True: 
        if is_prime(i):
            return i
        i += 1

def get_divisors(number: int) -> list:
    return [i for i in range(2, number) if number % i == 0] 

def get_valid_number() -> int:
    while True:
        user_input = input("Please enter the number to check: ")
        if user_input.isdigit() and int(user_input) > 0: 
            return int(user_input)
        print("That is not a positive whole number. Try again.")

def main():
    number = get_valid_number() 
    prev_prime = get_previous_prime(number)
    next_prime = get_next_prime(number)

    if prev_prime:
        print(f"\nThe prime number before {number} is {prev_prime}.")
    else:
        print(f"\nThere is no prime number before {number}.")

    if is_prime(number):
        print(f"{number} is a prime number.")
    else:
        divisors = get_divisors(number) 
        print(f"{number} is not prime. Its factors are {', '.join(map(str, divisors))}.")

    print(f"The prime number after
