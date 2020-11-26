def binary_search(lst, to_find):

    low = 0
    high = len(lst) - 1

    while (low <= high):
        
        mid = (low + high) // 2
        guess = lst[mid]

        if guess == to_find:
            return mid
        
        elif guess > to_find:
            high = mid - 1

        else:
            low = mid + 1

    return -1

    # search for the element to_find inside lst
    # if found, return index of element
    # else return -1

# my_list = [1, 3, 5, 7, 9]
# print(binary_search(my_list, 91))