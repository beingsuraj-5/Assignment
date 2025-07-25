
# Prime Number Utility Script

### Author: Suraj

### Date: 2025-06-11

## Description

This Python script allows users to:

* Check if a number is prime
* Find the closest previous and next prime numbers
* Display the divisors of a non-prime number

The script prompts the user to input a positive whole number and provides detailed information based on the input.

---

## Features

* **Prime Checking**: Determines if a number is prime.
* **Next/Previous Prime Finder**: Finds the nearest prime numbers before and after the given number.
* **Divisor Display**: Lists all divisors for non-prime numbers.

---

## Functions Overview

* `is_prime(number: int) -> bool`:
  Returns `True` if the number is prime; otherwise, `False`.

* `get_previous_prime(number: int) -> int`:
  Returns the closest smaller prime number.

* `get_next_prime(number: int) -> int`:
  Returns the closest greater prime number.

* `get_divisors(number: int) -> list`:
  Returns a list of all proper divisors (excluding 1 and the number itself).

* `get_valid_number() -> int`:
  Continuously prompts the user for valid input until a positive whole number is entered.

* `main()`:
  Orchestrates the flow — handles user input, performs prime checking, and displays the results.

---

## How to Use

1. Run the script in a Python environment (`python script_name.py`).
2. Enter a **positive whole number** when prompted.
3. View the results including:

   * Whether it is prime
   * Previous and next prime numbers
   * Divisors (if not prime)

---

## Example

```
Please enter the number to check: 20

The prime number before 20 is 19.
20 is not prime. Its factors are 2, 4, 5, 10.
The prime number after 20 is 23.
```

---

## Requirements

* Python 3.x

No external libraries are required.

