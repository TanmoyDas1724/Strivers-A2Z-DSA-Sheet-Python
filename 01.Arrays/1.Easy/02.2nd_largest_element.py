arr=[1,2,4,7,7,5]
def second_largest_element(arr):
    largest=arr[0]
    second_largest=arr[0]
    for i in arr:
        if i>largest:
            second_largest=largest
            largest=i
        elif i>second_largest and i!=largest:
            second_largest=i
    return second_largest
print("Second largest element in the array is:",second_largest_element(arr))