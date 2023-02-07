####
# Quicksort Iterative algorithm taken from: https://www.geeksforgeeks.org/binary-search/
# accessed on 01/27/22
# License: none given
# Authors: none given

###
# CHANGELOG:
# -added if __name__== "__main__" to driver code
# Rename the function
# Modify the function to return a subsection of the list

# Python3 code to implement iterative Binary
# Search.

# It returns location of x in given array arr
# if present, else returns -1


def binary_search_sub(arr, l, r, x):
    while l <= r:

        mid = l + (r - l) // 2

        # Check if x is present at mid
        if arr[mid] == x:
            return mid

        # If x is greater, ignore left half
        elif arr[mid] < x:
            l = mid + 1

        # If x is smaller, ignore right half
        else:
            r = mid - 1

    # If we reach here, then the element
    # was not present
    return mid  # was -1


if __name__ == "__main__":
    # Driver Code
    arr = [2, 3, 4, 10, 40]
    x = 10

    # Function call
    result = binary_search_sub(arr, 0, len(arr) - 1, x)

    if result != -1:
        print("Element is present at index % d" % result)
    else:
        print("Element is not present in array")
