# Compare and swap elements based on direction
# direction = 1 → ascending, direction = 0 → descending
def compAndSwap(arr, i, j, direction):
    if (direction == 1 and arr[i] > arr[j]) \
        or (direction == 0 and arr[i] < arr[j]):
        arr[i], arr[j] = arr[j], arr[i]

# Recursively merge a bitonic sequence into sorted order
def bitonicMerge(arr, low, cnt, direction):
    if cnt > 1:
        k = cnt // 2
        for i in range(low, low + k):
            compAndSwap(arr, i, i + k, direction)
        bitonicMerge(arr, low, k, direction)
        bitonicMerge(arr, low + k, k, direction)

# Recursively build bitonic sequences and sort them
def bitonicSort(arr, low, cnt, direction):
    if cnt > 1:
        k = cnt // 2

        # Sort first half ascending
        bitonicSort(arr, low, k, 1)

        # Sort second half descending
        bitonicSort(arr, low + k, k, 0)

        # Merge entire sequence in given direction
        bitonicMerge(arr, low, cnt, direction)

# function to sort the entire array
def sortArray(arr):

    # up = 1 → ascending, up = 0 → descending
    up = 1
    bitonicSort(arr, 0, len(arr), up)