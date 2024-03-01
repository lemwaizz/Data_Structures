#!/usr/bin/python3
"""
This is a binary search function
"""
file_path = "~/Data_Structures/numbers.txt"
def import_numbers(file_path):
    with open(file_path, 'r') as file:
        numbers = file.readlines()
    return [int(number.strip()) for number in numbers]

# Usage
numbers_list = import_numbers('numbers.txt')
print(numbers_list)

def binary_search(list, item):
    """this is a binary search function"""

    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high)//2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            high = mid + 1
    return None
print(binary_search(numbers_list, 13))
