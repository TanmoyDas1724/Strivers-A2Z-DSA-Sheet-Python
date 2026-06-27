arr=[1,1,2,2,2,3,3]
'''
def check_duplicate(arr):
    new_arr=[]
    for i in arr:
        if i not in new_arr:
            new_arr.append(i)
    return new_arr

'''

"""
Since the array is sorted, all duplicate elements are adjacent.
Use two pointers:
j → points to the last unique element.
i → traverses the array.
Start j = 0.
For every i from 1 to n-1:
If arr[i] != arr[j], a new unique element is found.
Increment j and copy arr[i] to arr[j].
After the loop, the first j+1 positions contain all unique elements.

"""
def remove_duplicates(arr):
    j = 0
    for i in range(1, len(arr)):
        if arr[i] != arr[j]:
            j += 1
            arr[j] = arr[i]

    return j + 1

length = remove_duplicates(arr)

print(arr[:length])
