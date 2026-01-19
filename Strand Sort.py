def merge(sorted_list, strand):
    result = []
    i = j = 0

    while i < len(sorted_list) and j < len(strand):
        if sorted_list[i] <= strand[j]:
            result.append(sorted_list[i])
            i += 1
        else:
            result.append(strand[j])
            j += 1

    result.extend(sorted_list[i:])
    result.extend(strand[j:])
    return result

def strand_sort(arr):
    sorted_list = []

    while arr:
        strand = [arr.pop(0)]
        i = 0
        while i < len(arr):
            if arr[i] > strand[-1]:
                strand.append(arr.pop(i))
            else:
                i += 1

        sorted_list = merge(sorted_list, strand)

    return sorted_list
