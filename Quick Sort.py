"""Implement quick sort in Python.
Input a list.
Output a sorted list."""


def swap(start_index, finish_index, array):
    temp = array[start_index]
    array[start_index] = array[finish_index]
    array[finish_index] = temp


def quicksort(array):
    index_pivot = -1
    def partition():
        nonlocal index_pivot
        out_of_list = False
        bigger_from_pivot = False
        index_pivot = int((len(array) - 1) / 2)
        low_index = 0
        high_index = len(array) - 1
        while low_index <= high_index:
            if low_index <= index_pivot:
                while array[low_index] <= array[index_pivot]:
                    low_index += 1
                    if low_index > index_pivot:
                        bigger_from_pivot = True
                        break
                if bigger_from_pivot:
                    continue
                while array[high_index] > array[index_pivot]:
                    high_index -= 1
                swap(low_index, high_index, array)
                if high_index is index_pivot:
                    index_pivot = low_index

            else:
                while array[low_index] > array[index_pivot]:
                    low_index += 1
                    if low_index > (len(array) - 1):
                        out_of_list = True
                        break
                if out_of_list:
                    break
                swap(low_index, index_pivot, array)
                temp_index = low_index
                low_index = index_pivot
                index_pivot = temp_index
            out_of_list = False
            bigger_from_pivot = False
    if len(array) is 1 or len(array) is 0:
        return array
    else:
        partition()
        left = quicksort(array[:index_pivot])
        right = quicksort(array[(index_pivot + 1):])
        return left + [array[index_pivot]] + right


test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
test1 = [4, 5, 2, 2, 3, 1, 8]
test3 = [2, 9, 15, 17, 12, 5, 4, 1, 3]
test4 = [2, 3, 4, 6, 1, 90, 100, 200, 10443, 3543, 32423, 1, 867, 32423]
test5 = [38, 81, 22, 48, 13, 69, 93, 14, 45, 58, 79, 72]
print(quicksort(test5))
