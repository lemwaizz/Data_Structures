import sys

class MergeSorting:
    @staticmethod
    def merge_sort(lst):
        if len(lst) <= 1:
            return lst
        middle = len(lst) // 2
        left = lst[:middle]
        right = lst[middle:]
        
        sleft = MergeSorting.merge_sort(left)
        sright = MergeSorting.merge_sort(right)
        
        return MergeSorting.merge(sleft, sright)

    @staticmethod
    def merge(left, right):
        result = []
        while left and right:
            if left[0] < right[0]:
                result.append(left[0])
                left.pop(0)
            else:
                result.append(right[0])
                right.pop(0)
        if left:
            result += left #for remainders left
        if right:
            result += right
        return result

if __name__ == "__main__":
    if len(sys.argv) > 1:
        lst = list(map(int, sys.argv[1:]))
        sorted_lst = MergeSorting.merge_sort(lst)
        print("Sorted List:", sorted_lst)
    else:
        print("Please provide a list of integers as command-line arguments.")
