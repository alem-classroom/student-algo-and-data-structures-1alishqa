def linear_search(lst, to_find):

  count = 0

  for i in lst:
    if i == to_find:
      return count
    count = count + 1

  return -1
  
  # search for the element to_find inside lst
  # if found, return index of element
  # else return -1

# print(linear_search(([5, 6, 'seven', 10]), 'seven'))
# print(linear_search(([5, 6, 'seven', 10]), 'sevenTY'))