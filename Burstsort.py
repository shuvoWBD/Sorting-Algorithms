def merge(arr1, arr2):
    arr3 = []
    i, j = 0, 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            arr3.append(arr1[i])
            i += 1
        else:
            arr3.append(arr2[j])
            j += 1

    while i < len(arr1):
        arr3.append(arr1[i])
        i += 1

    while j < len(arr2):
        arr3.append(arr2[j])
        j += 1

    return arr3

def split(arr):
    mid = len(arr) // 2
    subarr1 = arr[:mid]
    subarr2 = arr[mid:]
    return subarr1, subarr2

def burstSort(arr):
    # Base case: if array size is 1, return it
    if len(arr) == 1:
        return arr

    # Split the array into two sub-arrays
    subarr1, subarr2 = split(arr)

    # Sort the two sub-arrays
    arr1 = burstSort(subarr1)
    arr2 = burstSort(subarr2)

    # Merge the sorted arrays into a single sorted array
    return merge(arr1, arr2)

arr = [1, 5, 3, 7, 2, 4, 6]
arr = burstSort(arr)
print(arr)
