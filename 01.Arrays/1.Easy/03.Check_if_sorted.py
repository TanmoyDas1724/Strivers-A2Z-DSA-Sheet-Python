arr=[5,2,2,3,4,5]
#arr=[1,2,2,3,4,5]
def check_sorted(arr):
    for i in range(len(arr)-1):
        if arr[i]>arr[i+1]:
            return False
    return True

print("Is the array sorted?", check_sorted(arr))