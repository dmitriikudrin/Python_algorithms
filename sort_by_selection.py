def find_smallest(arr):
    smalest = arr[0]
    smalest_idx = 0
    for i in range(1, len(arr)):
        if arr[i] < smalest:
            smalest = arr[i]
            smalest_idx = i
    return smalest_idx


def sort_by_selection(arr):
    new_arr = []
    for i in range(0, len(arr)):
        idx = find_smallest(arr)
        new_arr.append(arr.pop(idx))
    return new_arr


my_list = [3, 5, 1, 9, 2]

print(sort_by_selection(my_list))
