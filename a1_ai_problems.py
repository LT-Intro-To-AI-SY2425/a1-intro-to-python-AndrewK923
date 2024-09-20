# Complete your individualized AI problems here

from tokenize import Intnumber
import math 
import random 

def fizbuzz(input_num):
    if(input_num%3==0):
        if(input_num%5==0):
            return 'FizzBuzz'
        return 'Fizz'
    elif(input_num%5==0):
        return 'Buzz'
    else:
        return input_num

assert fizbuzz(1) == 1, "fizzbuzz 1 test"
assert fizbuzz(3) == "Fizz", "fizzbuzz 3 test"
assert fizbuzz(4) == 4, "fizzbuzz 4 test"
assert fizbuzz(5) == "Buzz", "fizzbuzz 5 test"
assert fizbuzz(6) == "Fizz", "fizzbuzz 6 test"
assert fizbuzz(15) == "FizzBuzz", "fizzbuzz 15 test"
"""
Sure! Here are some beginner-level Python programming challenges to help you practice and improve your skills:

FizzBuzz: Write a program that prints numbers from 1 to 100. For multiples of 3, print "Fizz" instead of the number. For multiples of 5, print "Buzz". For numbers that are multiples of both 3 and 5, print "FizzBuzz".

Palindrome Checker: Write a function that checks if a given string is a palindrome (i.e., it reads the same backward as forward). Ignore spaces, punctuation, and capitalization.

Factorial Calculation: Write a function that calculates the factorial of a number. The factorial of a non-negative integer 
𝑛
n is the product of all positive integers less than or equal to 
𝑛
n.

Fibonacci Sequence: Write a function that returns the nth number in the Fibonacci sequence. The sequence starts with 0 and 1, and each subsequent number is the sum of the previous two.

Count Vowels: Write a function that takes a string and returns the number of vowels in that string. Consider 'a', 'e', 'i', 'o', and 'u' as vowels.

Sum of Digits: Write a function that takes an integer and returns the sum of its digits. For example, for the input 123, the output should be 6 (1 + 2 + 3).

Reverse a String: Write a function that takes a string and returns it in reverse order. For example, if the input is "hello", the output should be "olleh".

Even or Odd: Write a function that takes an integer as input and returns whether it is even or odd.

Prime Number Checker: Write a function that checks if a number is a prime number. A prime number is a number greater than 1 that has no positive divisors other than 1 and itself.

Guess the Number: Write a simple number guessing game. The program should generate a random number between 1 and 100 and then prompt the user to guess the number. Provide hints if the guess is too high or too low.

Feel free to start with any of these challenges, and let me know if you need help or further guidance!#
"""
#Fizzbuzz: take a number print 3 if its a multiple of 3 print Fuzz, if multiple of 5 print buzz, if both print fizzbuzz
def fizzBuzz():
    in_num = int(input("Input a number: "))
    if(in_num%3==0):
        if(in_num%5==0):
            return print("FizzBuzz")
        print("Fizz")
        return "Fizz"
    if(in_num%5==0):
        print("Buzz")
        return "Buzz"
    else:
        print(in_num)
        return in_num 
#fizzBuzz()

def even_or_odd():
    in_num = int(input("Input a number: "))
    if(in_num%2==0):
        print("Number is even!")
    else:
        print("Number is odd!") 
#even_or_odd()

def count_vowels():
    in_word = str(input("Input a word: "))
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    vowel_count = 0
    for letter in in_word:
        if letter in vowels:
            vowel_count += 1
    print("The word", in_word, "has", vowel_count, "vowel(s)")
#count_vowels()
        
def higher_or_lower():
    num = random.randint(1,100) 
    in_num = int(input("Guess the number between 1-100! I will tell you if you are higher or lower: "))
    condition = False
    while condition == False:
        if in_num == num:
            print("You guessed the number!")
            condition = True
            return
        elif in_num < num:
            print("Too low")
            in_num = int(input("Try Again:"))
        elif in_num > num:
            print("Too high")
            in_num = int(input("Try Again:"))
#higher_or_lower() 

def prime_number_checker():
    in_num = int(input("Input a number and I will tell you if its a prime number: "))
    if in_num <= 1:
        return False 
    for i in range(2, int((in_num**0.5) + 1)):
        if in_num % i == 0:
            print("It's not prime")
            return False 
    print("It's prime")
    return True 
#prime_number_checker() 