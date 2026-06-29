def union(arr1,arr2):
    ans=[]
    i=0
    j=0
    while i<len(arr1) and j<len(arr2):
        if arr1[i]<arr2[j]:
            ans.append(arr1[i])
            i+=1
        elif arr1[i]>arr2[j]:
            ans.append(arr2[j])
            j+=1
        else:
            ans.append(arr1[i])
            i+=1
            j+=1
    # Append any remaining elements from either array
    while i<len(arr1):
        ans.append(arr1[i])
        i+=1
    while j<len(arr2):
        ans.append(arr2[j])
        j+=1
    return ans

arr1=[2,4,6,8,10]
arr2=[1,2,3,4,5]
print("The union of two sorted arrays is :",union(arr1,arr2))