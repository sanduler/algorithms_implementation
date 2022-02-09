# Ruben Sanduleac
# implmination of binary_search iteretivly
# best case: O(1)
# average case: O(log n)
# worst case: O(log n)
# The space complexity of the binary search is O(1).

import random

def binary_search(list_of_numbers, target):
    """[This function returns the index of the target element]

    Args:
        list_of_numbers ([list]): [contains the numbers to binary search]
        target ([int]): [random integer from the list used to binary search]

    Returns:
        [int]: [returns the index location of the target element]
    """
    # set the higher bound of the search
    high = len(list_of_numbers)-1
    # set the lower bound of the search
    low = 0
    # while the higher bound is greater or equal to the lower
    while high >= low:

        # find the middle index location
        middle_index = (high + low) // 2

        # if the number in the middle index location is the target the return the index
        if list_of_numbers[middle_index] == target:
            return middle_index
        # if the number in the middle index location for the number is to big
        elif list_of_numbers[middle_index] > target:
            # set  the higher bond to be the middle index location
            high = middle_index - 1
        # # set  the lower bond to be the middle index location when the number of index larger then the target
        else:
            low = middle_index + 1
    # if no numbers are in the list
    return None


def start():
    # random list of sorted integers
    list_of_numbers = [1,2,5,7,9,11,12,13,15,17,18,21,23,
                    25,29,31,33,35,36,37,38,39,
                    41,42,45,47,48,52,57,60,63,65,67,68,69,70,72,
                    73,75,77,80,81,85,87,89,95,96,97,99,100]

    # determine the target number from the list
    target = random.choice(list_of_numbers)

    # print the outcome
    print(f"The random target integer is {target}")
    print(f"The location of the integer is on index {binary_search(list_of_numbers, target)}")

start()