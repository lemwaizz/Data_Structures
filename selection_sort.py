import random

class random_list:
    """This is a selection sort algorithm"""

    def __init__(self, w=None, x=None, y=None, z=None):
        """to generate random list"""
        self.__w = w
        self.__x = x
        self.__y = y
        self.__z = z
        self.random_list = []
        for i in range(w, x):
            n = random.randint(y, z)
            self.random_list.append(n)
        print(self.random_list)
    
    # Properties and setters omitted for brevity

class selection_sort(random_list):
    """selection sort class that inherits from class random_list."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Additional initialization specific to selection_sort class

    def FindSmallest(self, random_list_instance):
        """finds the smallest element in the list"""
        smallest = random_list_instance[0]
        smallest_index = 0
        for i in range(len(random_list_instance)):
            if random_list_instance[i] < smallest:
                smallest_index = i
                smallest = random_list_instance[i]
        return smallest_index

    def SelectionSort(self, random_list_instance):
        """sorts the list using selection sort"""
        newArr = []
        for i in range(len(random_list_instance)):
            smallest = self.FindSmallest(random_list_instance)
            newArr.append(random_list_instance.pop(smallest))
        return newArr

w = int(input("Lowest range of your list:"))
x = int(input("Upper range of your list:"))
y = int(input("Lower range of sample for integers in list:"))
z = int(input("Upper range of sample for integers in list:"))

# Creating an instance of selection_sort class
sorter = selection_sort(w, x, y, z)

# Calling the SelectionSort method
sorted_list = sorter.SelectionSort(sorter.random_list[:])

print("Sorted List:", sorted_list)
