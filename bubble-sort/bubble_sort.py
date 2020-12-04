def bubble_sort(lst):

    swapped = True
    while swapped:

        swapped = False

        for i in range (len(lst) - 1):

            if lst[i] > lst[i + 1]:

                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                swapped = True

    return lst    
    # sort the list via bubble sort

# l = [5, 4, 3, 2, 1, 0, -1]
# print(bubble_sort(l))