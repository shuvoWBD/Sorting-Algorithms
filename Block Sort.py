# Python Implementation


def block_sort(arr, block_size):

    # Create an empty list to
    # hold the sorted blocks
    blocks = []

    # Divide the input array into
# blocks of size block_size

    for i in range(0, len(arr), block_size):

        block = arr[i:i + block_size]

        # Sort each block and append
        # it to the list of sorted blocks
        blocks.append(sorted(block))

    # Merge the sorted blocks into
    # a single sorted list
    result = []
    while blocks:

        # Find the smallest element in
        # the first block of
        # each sorted block
        min_idx = 0
        for i in range(1, len(blocks)):
            if blocks[i][0] < blocks[min_idx][0]:
                min_idx = i

        # Remove the smallest element and
        # append it to the result list
        result.append(blocks[min_idx].pop(0))

        # If the block is now empty, remove
        # it from the list of sorted blocks
        if len(blocks[min_idx]) == 0:
            blocks.pop(min_idx)
    return result


# Original arr
arr = [1, 7, 8, 2, 3, 5, 4, 6]
print('Input: ', arr)

# Select box size
block_size = 3

# Function call
print('Output:', block_sort(arr, block_size))