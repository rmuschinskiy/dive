__author__ = 'Sindbad'

# Question 8: Longest Repetition

# Define a procedure, longest_repetition, that takes as input a
# list, and returns the element in the list that has the most
# consecutive repetitions. If there are multiple elements that
# have the same number of longest repetitions, the result should
# be the one that appears first. If the input list is empty,
# it should return None.


def longest_repetition(elements):
    best_element = None
    length = 0
    current_length = 0
    current = None
    for el in elements:
        if current!=el:
            current=el
            current_length = 1
        else:
            current_length += 1
        if current_length > length:
            best_element = current
            length = current_length
    return best_element





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
