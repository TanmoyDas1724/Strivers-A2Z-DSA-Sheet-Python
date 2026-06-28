"""
1. Brute Force Solution
Approach
Create a temporary array.
Traverse the original array and store all non-zero elements in the temporary array.
Count how many zeros are left.
Append those zeros at the end.
Copy the temp array back to the original array.
Time Complexity
O(N)
Space Complexity
O(N)

"""
"""
def move_zeros(arr):
    temp=[]
    for i in arr:
        if i!=0:
            temp.append(i)
    zeros=len(arr)-len(temp)
    for i in range(zeros):
        temp.append(0)
    return temp
arr=[1,0,2,0,3,4,0,5]
print("The updated array is :",move_zeros(arr))
    
"""

"""
2. Optimal Solution (Two Pointers)
Approach
Find the first zero position (j).
Traverse the array from j+1.
Whenever a non-zero element is found:
Swap it with arr[j].
Increment j.
All zeros automatically move to the end.
Time Complexity
O(N)
Space Complexity
O(1)
"""
def move_zeros(arr):
    j=-1
    for i in range(len(arr)):
        if arr[i]==0:
            j=i
            break 
    if j==-1:
        return arr
    for i in range(j+1,len(arr)):
        if arr[i]!=0:
            arr[j],arr[i]=arr[i],arr[j]
            j+=1
    return arr
arr = [1, 0, 2, 0, 3, 4, 0]
print(move_zeros(arr))