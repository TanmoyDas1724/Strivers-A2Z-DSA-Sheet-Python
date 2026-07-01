def Number_That_appears_ones(arr):
    i=0
    while i<len(arr)-1:
        if arr[i]==arr[i+1]:
            i+=2
        else:
            return arr[i]
arr=[1,1,2,2,3,3,4,5,5]
print("Number that appears once:", Number_That_appears_ones(arr))