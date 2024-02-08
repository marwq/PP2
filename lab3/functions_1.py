# 1. A recipe you are reading states how many grams you need for the ingredient. Unfortunately, your store only sells items in ounces. Create a function to convert grams to ounces. ounces = 28.3495231 * grams

def grams_to_ounces(grams: float) -> float:
    ounces = 28.3495231 * grams
    return ounces


# 2. Read in a Fahrenheit temperature. Calculate and display the equivalent centigrade temperature. The following formula is used for the conversion: C = (5 / 9) * (F – 32)

def fahrenheit_to_centigrade(fahrenheit: float) -> float:
    centigrade = (5 / 9) * (fahrenheit - 32)
    return centigrade


# 3. Write a program to solve a classic puzzle: We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have? create function: solve(numheads, numlegs):

def solve(numheads: int, numlegs: int) -> tuple[int, int] | None:
    for i in range(numheads+1):
        j = numheads - i
        if 2*i + 4*j == numlegs:
            return i, j
    return None

print(solve(35, 94))


# 4. You are given list of numbers separated by spaces. Write a function filter_prime which will take list of numbers as an agrument and returns only prime numbers from the list.

def is_prime(num: int) -> bool:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return num > 1

def filter_prime(numbers: list[int]) -> list[int]:
    prime_numbers = list(filter(is_prime, numbers))
    return prime_numbers

input_ = '1 2 3 4 5 6 7 8 9 10'
filter_prime(map(int, input_.split()))


# 5. Write a function that accepts string from user and print all permutations of that string.

from itertools import permutations

def string_permutations(string: str) -> list[str]:
    return list(permutations(string))


# 6. Write a function that accepts string from user, return a sentence with the words reversed. We are ready -> ready are We

def reverse_words(string: str) -> str:
    return " ".join(string.split()[::-1])


# 7. Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

'''
has_33([1, 3, 3]) → True
has_33([1, 3, 1, 3]) → False
has_33([3, 1, 3]) → False
'''

def has_33(numbers: list[int]) -> bool:
    for i in range(len(numbers)-1):
        if numbers[i] == 3 and numbers[i+1] == 3:
            return True
    return False


# 8. Write a function that takes in a list of integers and returns True if it contains 007 in order

'''
spy_game([1,2,4,0,0,7,5]) --> True
spy_game([1,0,2,4,0,5,7]) --> True
spy_game([1,7,2,0,4,5,0]) --> False
'''

def spy_game(numbers: list[int]) -> bool:
    code = [0, 0, 7]
    for num in numbers:
        if num == code[0]:
            code.pop(0)
            if len(code) == 0:
                return True
    return False


# 9. Write a function that computes the volume of a sphere given its radius.

def sphere_volume(radius: float) -> float:
    return (4/3) * 3.14 * radius**3


# 10. Write a Python function that takes a list and returns a new list with unique elements of the first list. Note: don't use collection set.

def unique_elements(numbers: list[int]) -> list[int]:
    unique_numbers = {i: None for i in numbers}
    return list(unique_numbers.keys())


# 11. Write a Python function that checks whether a word or phrase is palindrome or not. Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam

def is_palindrome(string: str) -> bool:
    return string == string[::-1]


# 12. Define a functino histogram() that takes a list of integers and prints a histogram to the screen. For example, histogram([4, 9, 7]) should print the following:

'''
****
*********
*******
'''

def histogram(numbers: list[int]) -> None:
    for num in numbers:
        print("*" * num)
        

# 13. Write a program able to play the "Guess the number" - game, where the number to be guessed is randomly chosen between 1 and 20. This is how it should work when run in a terminal:

'''
Hello! What is your name?
KBTU

Well, KBTU, I am thinking of a number between 1 and 20.
Take a guess.
12

Your guess is too low.
Take a guess.
16

Your guess is too low.
Take a guess.
19

Good job, KBTU! You guessed my number in 3 guesses!
'''

import random

def guess_the_number() -> None:
    number = random.randint(1, 20)
    print("Hello! What is your name?")
    name = input()
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    guess = 0
    count = 0
    while guess != number:
        print("Take a guess.")
        guess = int(input())
        count += 1
        if guess < number:
            print("Your guess is too low.")
        elif guess > number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {count} guesses!")