def find_common_elements(arr1, arr2):
    common_elements = []
    i, j = 0, 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            i += 1  
        elif arr1[i] > arr2[j]:
            j += 1  
        else:
            if not common_elements or common_elements[-1] != arr1[i]:
                common_elements.append(arr1[i])
            i += 1
            j += 1

    return common_elements

arr1 = [1, 2, 3, 4, 5, 6]
arr2 = [4, 5, 6, 7, 8, 9]

result = find_common_elements(arr1, arr2)
print("Common elements:", result)
