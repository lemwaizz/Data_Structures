#!/usr/bin/python3
"""
This is a binary search function
"""
file_path = "numbers.txt"
def import_numbers(file_path):
    with open(file_path, 'r') as file:
        numbers = file.readlines()
        numbers = [int(number.strip()) for number in numbers]
        numbers.sort()
    return numbers
# Usage
numbers_list = import_numbers('numbers.txt')
item = int(input("what number are you looking for: "))
print(numbers_list)
if __name__ == "__main__":
    def binary_search(numbers_list, item):
        """this is a binary search function"""

        low = 0
        high = (len(numbers_list)) - 1
        while low <= high:
            mid = (low + high)//2
            guess = numbers_list[mid]
            if guess == item:
                return mid
            if guess > item:
                high = mid - 1
            else:
                low = mid + 1
        return None
    print(binary_search(numbers_list, item))
