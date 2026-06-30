"""
Idea

Since both arrays are already sorted:

If elements are equal → they are part of the intersection.
If one element is smaller, move that pointer because it cannot match any previous element in the other array.

"""

def intersection(arr1, arr2):
    i = 0
    j = 0
    ans = []

    while i < len(arr1) and j < len(arr2):

        if arr1[i] == arr2[j]:
            ans.append(arr1[i])
            i += 1
            j += 1

        elif arr1[i] < arr2[j]:
            i += 1

        else:
            j += 1

    return ans


arr1 = [1,1,1,1,1,1,1,2,2]
arr2 = [1,2,3,4,5]

print(intersection(arr1, arr2))