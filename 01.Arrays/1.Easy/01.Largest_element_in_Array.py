arr=[2,4,1,8,3]
def largest_element(arr):
    largest=arr[0]
    for i in arr:
        if i>largest:
            largest=i
    return largest
print("Largest element in the array is:",largest_element(arr))