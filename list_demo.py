import random

list_of_numbers = [6, 5, 3, 8, 4, 2, 5, 11, 53, 17, 27, 99, 62, 61, 51, 47]
empty_list = []

for number in list_of_numbers:
    print(number)

print("\n\n")

number_of_items_in_list = len(list_of_numbers)
for index in range(number_of_items_in_list):
    print(f"Item {index + 1}: {list_of_numbers[index]}")

print("\n Random values from list")
for number in range(3):
    index = random.randint(0, number_of_items_in_list -1)

print("\n Append random values to the list")
for num in range(3):
    random_value = random.randint(0,100)
    list_of_numbers.append(random_value)

print(list_of_numbers)
    