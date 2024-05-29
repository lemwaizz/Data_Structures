import sys

class BinarySearch:
    """Class that contains our binary search functions."""
    @staticmethod
    def binary_search(array, target, low, high):
        if low > high:
            return -1  # Target not found
        
        mid = (low + high) // 2
        guess = array[mid]
        
        if guess == target:
            return mid
        elif guess < target:
            return BinarySearch.binary_search(array, target, mid + 1, high)
        else:
            return BinarySearch.binary_search(array, target, low, mid - 1)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <list> <target>")
        sys.exit(1)
    
    try:
        array = list(map(int, sys.argv[1].strip('[]').split(',')))
        target = int(sys.argv[2])
        
        array.sort()  # Ensure the array is sorted
        result = BinarySearch.binary_search(array, target, 0, len(array) - 1)
        
        if result != -1:
            print(f"Target found at index: {result}")
        else:
            print("Target not found in the array.")
    
    except ValueError:
        print("Check inputs. Make sure the list is a comma-separated string of integers and the target is an integer.")
        sys.exit(1)
