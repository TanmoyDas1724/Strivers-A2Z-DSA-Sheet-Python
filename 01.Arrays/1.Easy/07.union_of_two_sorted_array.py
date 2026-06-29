def union(arr1, arr2):
    ans = []
    i = 0
    j = 0

    while i < len(arr1) and j < len(arr2):

        if arr1[i] < arr2[j]:
            if arr1[i] not in ans:
                ans.append(arr1[i])
            i += 1

        elif arr1[i] > arr2[j]:
            if arr2[j] not in ans:
                ans.append(arr2[j])
            j += 1

        else:
            if arr1[i] not in ans:
                ans.append(arr1[i])
            i += 1
            j += 1

    while i < len(arr1):
        if arr1[i] not in ans:
            ans.append(arr1[i])
        i += 1

    while j < len(arr2):
        if arr2[j] not in ans:
            ans.append(arr2[j])
        j += 1

    return ans


arr1 = [1,1,1,1,1,1,1,2,2]
arr2 = [1,2,3,4,5]

print("The union of two sorted arrays is :", union(arr1, arr2))