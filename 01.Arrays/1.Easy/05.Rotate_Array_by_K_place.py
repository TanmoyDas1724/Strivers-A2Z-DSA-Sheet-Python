# BRUTE FORCE SOLUTION
"""
arr = [1,2,3,4,5,6,7]
k = 3

Store first k elements:

temp = [1,2,3]

Shift remaining elements left:

[4,5,6,7,5,6,7]

Copy temp to the end:

[4,5,6,7,1,2,3]
"""
"""
def left_rotate(arr, k):
    n = len(arr)
    k = k % n

    temp = arr[:k]

    for i in range(k, n):
        arr[i-k] = arr[i]

    for i in range(k):
        arr[n-k+i] = temp[i]

    return arr

arr = [1,2,3,4,5,6,7]
print(left_rotate(arr, 3))

"""

# OPTIMIZED SOLUTION
"""
Approach

For right rotation by k:

Reverse the entire array.
Reverse the first k elements.
Reverse the remaining n-k elements.
Example
arr = [1,2,3,4,5,6,7]
k = 3
Step 1: Reverse whole array
[7,6,5,4,3,2,1]
Step 2: Reverse first k elements
[5,6,7,4,3,2,1]
Step 3: Reverse remaining elements
[5,6,7,1,2,3,4]
"""

def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

def rotate(arr, k):
    n = len(arr)
    k = k % n

    reverse(arr, 0, n-1)
    reverse(arr, 0, k-1)
    reverse(arr, k, n-1)

    return arr

arr = [1,2,3,4,5,6,7]
print(rotate(arr, 3))