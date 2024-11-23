import json
import time
import signal
from random import Random

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

numbers_count = int(input("How many numbers would you like to recall? "))

seconds = 7

for i in range(numbers_count):
    random_num = Random().randint(0, 99)
    print("Enter the mnemonic for the number " + str(random_num).zfill(2) + ": ")

    # Set the alarm for 5 seconds
    signal.alarm(seconds)

    mnemonic = input()
    # Disable the alarm
    signal.alarm(0)

    if mnemonic == mnemonics_dict[str(random_num).zfill(2)]:
        print("Correct!")
        rights += 1
    else:
        print("Wrong mnemonic entered. Please try again.")
        i -= 1

print("You got " + str(rights) + " out of " + str(numbers_count) + " right.")
