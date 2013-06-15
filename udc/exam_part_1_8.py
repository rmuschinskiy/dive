__author__ = 'Sindbad'

# Question 8: Longest Repetition

# Define a procedure, longest_repetition, that takes as input a
# list, and returns the element in the list that has the most
# consecutive repetitions. If there are multiple elements that
# have the same number of longest repetitions, the result should
# be the one that appears first. If the input list is empty,
# it should return None.


def longest_repetition(elements):
    prev = None
    counter = 1
    run_counter = 0
    count_keeper = []
    for el in elements:
        if el == prev:
            counter += 1
        else:
            if prev is not None:
                count_keeper.append([prev,counter])
                counter = 1
        prev = el
        run_counter += 1
        if run_counter==len(elements):
            count_keeper.append([prev,counter])
    return count_keeper




def remove_duplicates(item_list):
    result = []
    for elem in item_list:
        if elem not in result:
            result.append(elem)
    return result



#For example,

print longest_repetition([[1], [2, 2], [2, 2], [2, 2], [3, 3, 3]])
# [2,2]

print longest_repetition([1, 2, 2, 3, 3, 3, 2, 2, 1])
# 3

print longest_repetition(['a', 'b', 'b', 'b', 'c', 'd', 'd', 'd'])
# b

print longest_repetition([1,2,3,4,5])
# 1

print longest_repetition([])
# None
