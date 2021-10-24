#!/usr/bin/env python

import random
from os import system, name


def clear_screen():
    system('clear')


def evaluate_guess(code, a_guess):
    outcome = list()
    for i in range(0, 5):
        if code[i] == a_guess[i]:
            outcome.append('2')
    overlap = len(set(code) & set(a_guess))
    already_counted = len(outcome)

    for i in range(0, (overlap - already_counted)):
        outcome.append('1')

    for i in range(len(outcome), 5):
        outcome.append('0')
    return outcome


def pretty_list(str_list):
    return "[{}]".format(', '.join(str_list))


def pretty_compact_list(str_list):
    return ''.join(str_list)


def valid_guess(guess_input):
    return len(guess_input) == 5 and len(set(guess_input)) == 5


def get_random_code():
    digits = list(range(1,9))
    candidate = []
    while len(candidate) < 5:
        x = random.choice(digits)
        if x not in candidate:
            candidate.append(x)
    return list(map(str, candidate))


clear_screen()
secret_code = get_random_code()
print("Welcome to the code breaker game,  for simplicity we will use digits as opposed to colors")
print("Acceptable digits will be from 1 to 8,  combining the 8 possible different values for each place")
print("the code will be a combination of 5 different digits, we cannot use the same digit multiple times in one code")
print("2 is black: means a digit is correct and in the right place")
print("1 is white: means a digit is correct by not in the right place")
print("0 is blank: means a digit is not even correct")

max_attempts = 15
print("You have {} attempts\n".format(max_attempts))

attempts = 0
won = False
guess = list(input("Add your guess: "))
while attempts < max_attempts and not won:
    attempts = attempts + 1
    result = evaluate_guess(secret_code, guess)
    result_display = "attempt {}: {}: {}".format(attempts, pretty_list(guess), pretty_compact_list(result))
    if set(result) == set('2'):
        print("{}\t\t Congratulations smarty pants,  this is correct".format(result_display))
        won = True
    elif attempts == max_attempts:
        print("{}\t\t Hard luck next game".format(result_display))
    else:
        guess = list(input("{}\t\t Next guess: ".format(result_display)))
        while not valid_guess(guess):
            guess = list(input("{}\t\t That was not correct, try again guess: ".format(result_display)))

print("code was {}".format(pretty_list(secret_code)))



