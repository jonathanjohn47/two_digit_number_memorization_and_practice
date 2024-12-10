import json
import time
import signal
from random import Random

import numpy

# Load the JSON file and convert it into a dictionary
with open('number_mnemonics.json', 'r') as file:
    mnemonics_dict = json.load(file)


# Function to handle the timeout
def timeout_handler(signum, frame):
    print("\nTime's up! You took too long to respond.")
    exit(1)


# Set the signal handler for SIGALRM
signal.signal(signal.SIGALRM, timeout_handler)

rights = 0
first_number = int(input("Enter First Number from where you want to start: "))
numbers_count = int(input("How many numbers would you like to recall? "))
is_random = input("Would you like the numbers to be random? (y/n) ")

timing = []

numbers_generated = []


def generateRandomNumber():
    new_random_num = Random().randint(first_number, first_number + numbers_count - 1)
    if new_random_num not in numbers_generated:
        numbers_generated.append(new_random_num)
        return new_random_num
    else:
        return generateRandomNumber()


for i in range(first_number, first_number + numbers_count):
    if is_random == "y":

        random_num = generateRandomNumber()

    else:
        random_num = i
    print("Time Remaining: 5 seconds")
    print("Enter the mnemonic for the number " + str(random_num).zfill(2) + ": ")

    start_time = time.time() * 1000
    signal.setitimer(signal.ITIMER_REAL, 5)

    mnemonic = input()
    signal.setitimer(signal.ITIMER_REAL, 0)
    end_time = time.time() * 1000
    timing.append(end_time - start_time)

    if mnemonic == mnemonics_dict[str(random_num).zfill(2)]:
        print("Correct!")
        rights += 1
    else:
        print("Wrong mnemonic entered. Please try again.")
        i -= 1

print("You got " + str(rights) + " out of " + str(numbers_count) + " right.")
average_time = numpy.average(timing)
print("Average time taken per number: " + str(average_time / 1000) + " seconds.")
