import random

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

random_list = list(range(20))
random_list.sort()
print(random_list)
print(binary_search(random_list, 13))