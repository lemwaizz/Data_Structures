#!/usr/bin/python3
"""
This is the list 
"""

import random
from Binary_search import binary_search

if __name__ == "__main__":
    random_list = list(range(20))
    random_list.sort()
    print(random_list)
    print(binary_search(random_list, 13))
