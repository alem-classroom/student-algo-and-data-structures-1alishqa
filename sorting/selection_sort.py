def selection_sort(lst):

    swapped = True
    while (swapped):

        swapped = False
        for i in range(len(lst) - 1):

            if (lst[i] > lst[i + 1]):

                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                swapped = True

    return lst
    # sort the list via selection sort

# list = ['aa', 'rr', 'avc', 'XYZ']
# print(list)
# list.sort()
# print(list, '\n')

# list2 = ['aa', 'rr', 'avc', 'XYZ']
# print(list2)
# print(selection_sort(list2), '\n')


# list3 = [5, -3, 15, 27, 0, 7]
# print(list3)
# list3.sort()
# print(list3, '\n')

# list4 = [5, -3, 15, 27, 0, 7]
# print(list4)
# print(selection_sort(list4))