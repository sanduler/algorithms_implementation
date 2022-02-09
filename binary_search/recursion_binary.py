# Ruben Sanduleac
# implmination of binary_search recursively
# best case: O(1)
# average case: O(log n)
# worst case: O(log n)
# The space complexity of the binary search is O(1).



def binary_search(list_of_numbers, low, high, target):
    
    # if the higher index is greater than the lower index
    if high >= low:
        # sum the higher index with the lower index and divide by two and round down
        mid = (high + low) // 2
        # if take the middle index and check if the number  in the array is the target number
        if list_of_numbers[mid] == target:
            # if the number is the target return the number back
            return mid
        # else if the number in the array is less than the target ( the number is on the left side)
        elif list_of_numbers[mid] > target:
            # return recursevly, set the higher index to to the middle index and subtract one
            return binary_search(list_of_numbers, low, mid-1, target)
         # else if the number in the array is greater than the target ( the number is on the left side)
        else:
            # return recursevly, set the low index to to the middle index and add one
            return binary_search(list_of_numbers, mid+1, high, target)
    # if the number is not in the list
    else:
        return None

list_of_numbers = [12,4,5,6,8,9,10,12,13,14,15,16,18,20,22,23,24,25,26,27,
                   28,30,31,32,34,36,38,40,42,44,46,48,49,50,51,52,54,56,58,
                   59,60,61,62,64,66,68,69,70,72,73,74,76,77,78,80,81,82,84,
                   86,87,88,90,92,94,95,96,97,98,99,100]


high =len(list_of_numbers) - 1
low = 0

for number in range(32, 56):
    target = number
    print(binary_search(list_of_numbers, low, high, target))
