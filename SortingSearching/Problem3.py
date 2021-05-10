# Search in a rotated array: Given an array that has been rotated an unknown
# number of times, search for an element.  Not stated in problem, but if there
# are repeats, I will return the lowest index.

from CrackingCode.SortingSearching.Search import binary_search


def find_transition_point(arr, low=0, high=None):
    # Transition point occurs at max in array, so this finds
    # index of max element in a possiibly rotated array
    if high is None:
        high = len(arr) - 1
    if arr[high] > arr[low] or low > high:
        return high
    med = (low + high) // 2
    if arr[med] <= arr[low]:
        return max(low, find_transition_point(arr, low, med - 1))
    else:
        return max(med, find_transition_point(arr, med, high))


def search(arr, item):
    max_idx = find_transition_point(arr)
    if item == arr[max_idx]:
        return max_idx
    elif arr[0] <= item <= arr[max_idx]:
        return binary_search(arr, item, 0, max_idx)
    else:
        return binary_search(arr, item, low=max_idx + 1, high=len(arr) - 1)


def main():
    arr = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7]
    # print(find_transition_point(arr))
    # print(find_transition_point([15, 16, 19, 20, 25, 27, 28, 1, 3, 4, 5, 7]))
    # print(find_transition_point([1, 2, 3]))

    assert search(arr, 20) == 3
    assert search(arr, 8) is None
    assert search(arr, 1) == 5
    assert search(arr, 15) == 0
    assert search(arr, 7) == 9

    arr = [16, 17, 4, 6, 7, 7, 10]
    assert search(arr, 7) == 4

    arr = [16, 17, 4, 6, 7, 7, 16]
    assert search(arr, 16) == 0

    arr = [2, 2, 2, 3, 4, 2]
    assert search(arr, 2) == 0


if __name__ == "__main__":
    main()
    print("Problem 3")
