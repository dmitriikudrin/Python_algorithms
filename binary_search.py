my_list = 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',\
          'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',\
          'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',\
          'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',


def binary_search(input_list, item):
    low = 0
    high = len(input_list) - 1

    while True:
        mid = (high + low) // 2
        if input_list[mid] == item:
            return mid
        elif input_list[mid] < item:
            low = mid + 1
        else:
            high = mid - 1


print(binary_search(my_list, 'z'))
