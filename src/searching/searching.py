def linear_search(arr, target):
    # Your code here
    for i in range(0, len(arr)):
        if arr[i] == target:
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    start = 0
    mid = 0
    end = len(arr) - 1
    
    while end >= start:
        mid = (end + start) // 2

        # target is further right
        if arr[mid] < target:
            start = mid + 1
        # target is further left
        elif arr[mid] > target:
            end = mid - 1
        else:
            # target is in middle
            return mid
    return -1  # not found
