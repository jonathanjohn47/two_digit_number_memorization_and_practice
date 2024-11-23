import random
import time

numbers = []

for _ in range(15):
  random_number = str(random.randint(0, 99)).zfill(2)
  numbers.append(random_number)
  print(random_number)
  time.sleep(10)

concatenated_numbers = "".join(numbers)
print("All numbers:", concatenated_numbers)

index = 0
while index < len(numbers):
  user_input = input("Enter the next number in the series: ")
  if user_input == numbers[index]:
    print("Correct!")
    index += 1
  else:
    print("Wrong number entered. Please try again.")