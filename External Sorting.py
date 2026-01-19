import heapq
import os
import random

# A class for Min Heap


class MinHeapNode:
    def __init__(self, element, i):
        # The element to be stored
        self.element = element

        # index of the array from which the element is taken
        self.i = i

# Merges k sorted files


def merge_files(output_file, n, k):
    harr = []
    out = open(output_file, "w")

    # Open output files in read mode.
    in_files = [open(str(i), 'r') for i in range(k)]

    # Create a min heap with k heap nodes.
    # Every heap node has first element of scratch output file
    for i in range(k):
        element = in_files[i].readline().strip()
        if element:
            heapq.heappush(harr, (int(element), i))

    count = 0
    while count < k:
        # Get the minimum element and store it in output file
        root = heapq.heappop(harr)
        out.write(str(root[0]) + '\n')

        # Find the next element that will 
        # replace current root of heap.
        element = in_files[root[1]].readline().strip()
        if element:
            heapq.heappush(harr, (int(element), root[1]))
        else:
            count += 1

    # close input and output files
    for i in range(k):
        in_files[i].close()
    out.close()

# Using a merge-sort algorithm, create the 
# initial runs and divide them evenly among the output files
def create_initial_runs(input_file, run_size, num_ways):
    in_file = open(input_file, "r")

    # output scratch files
    out_files = [open(str(i), 'w') for i in range(num_ways)]

    more_input = True
    next_output_file = 0

    while more_input:
        data = []
        for _ in range(run_size):
            line = in_file.readline().strip()
            if line:
                data.append(int(line))
            else:
                more_input = False
                break

        # sort array using merge sort
        data.sort()

        # write the records to the appropriate 
        # scratch output file
        for i in data:
            out_files[next_output_file].write(str(i) + '\n')

        next_output_file += 1

    # close input and output files
    for i in range(num_ways):
        out_files[i].close()

    in_file.close()

# For sorting data stored on disk


def external_sort(input_file, output_file, num_ways, run_size):
    # read the input file, create the initial runs, 
    # and assign the runs to the scratch output files
    create_initial_runs(input_file, run_size, num_ways)

    # Merge the runs using the K-way merging
    merge_files(output_file, run_size, num_ways)

# Driver code


def main():
    # No. of Partitions of input file.
    num_ways = 10

    # The size of each partition
    run_size = 1000

    input_file = "input.txt"
    output_file = "output.txt"

    # generate input
    with open(input_file, 'w') as f:
        for _ in range(num_ways * run_size):
            f.write(str(random.randint(0, 10000)) + '\n')

    external_sort(input_file, output_file, num_ways, run_size)


if __name__ == "__main__":
    main()