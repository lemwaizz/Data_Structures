import sys
lst = [9, 10, 0, 16, -5, 2]
class merge_sorting:
    @staticmethod
    def merge_sort(lst):
        if len(lst) <= 1:
            return lst
        middle = len(lst)//2
        left = lst[:middle]
        right = lst[middle:]
        sleft = merge_sort(left)
        sright = merge_sort(right)

    @staticmethod
    def merge(left, right):
        result = []
        while left and right:
            if left[0] < right[0]:
                result.append(left[o])
                left.pop(0)
            else:
                result.append(right[0])
                right.pop(0)
        if left:
            result += left
        if right:
            result += right
        return result
        print(result)
