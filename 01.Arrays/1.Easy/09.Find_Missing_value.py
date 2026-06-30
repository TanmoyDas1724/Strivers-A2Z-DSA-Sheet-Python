"""1. Brute Force Approach
Approach
Check every number from 1 to N.
For each number, search the entire array.
If a number is not found, it is the missing number.
Algorithm
Loop from 1 to N.
Search the current number in the array.
If not found, return it.
"""

"""
def missing_number(arr, N):

    for num in range(1, N + 1):
        found = False

        for value in arr:
            if value == num:
                found = True
                break

        if not found:
            return num


arr = [1,2,4,5]
N = 5
print(missing_number(arr, N))
"""

"""
Time Complexity
O(N²)
Space Complexity
O(1)

"""

"""
2. Better Approach (Hashing)
Approach
Create a frequency array of size N+1.
Mark every number present in the array.
The index with frequency 0 is the missing number.
"""
"""
def missing_number(arr, N):

    hash_arr = [0] * (N + 1)

    for num in arr:
        hash_arr[num] = 1

    for i in range(1, N + 1):
        if hash_arr[i] == 0:
            return i


arr = [1,2,4,5]
N = 5

print(missing_number(arr, N))
Time Complexity
O(N)
Space Complexity
O(N)
"""

"""
3. Optimal Approach (Sum Formula)
Idea

The sum of numbers from 1 to N is:

Sum=N*(N+1)//2
	​
Subtract the sum of the array from this expected sum.

Formula
Missing Number = N*(N+1)//2 - sum(arr)
"""
def missing_number(arr, N):

    expected_sum = N * (N + 1) // 2
    actual_sum = sum(arr)

    return expected_sum - actual_sum


arr = [1,2,4,5]
N = 5

print(missing_number(arr, N))
"""
Time Complexity
O(N)
Space Complexity
O(1)
"""