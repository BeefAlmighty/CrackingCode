# Implementation of common sorting algorithms.  All are done `in place', unless
# otherwise stated.


def sort(ls, reverse=False, kind="heap"):
    if reverse:
        comp = more
    else:
        comp = less

    if kind == "insertion":
        insertion_sort(ls, comp)
    elif kind == "selection":
        selection_sort(ls, comp)
    elif kind == "merge":
        mergesort(ls, comp)
    elif kind == "qsort":
        quicksort(ls, comp)
    else:
        heap_sort(ls, comp)

    return


def swap(ls, i, j):
    # swap ls[i] and ls[j] in place
    old_i = ls[i]
    ls[i] = ls[j]
    ls[j] = old_i
    return


def less(i, j):
    return i < j


def more(i, j):
    return i > j


def heap_left(i):
    return (2 * i) + 1


def heap_right(i):
    return (2 * i) + 2


def heap_parent(i):
    return i // 2 if i % 2 != 0 else i // 2 - 1


def bubble_down(ls, idx, heap_size, comp=less):
    left_idx = heap_left(idx)
    right_idx = heap_right(idx)

    if left_idx < heap_size and comp(ls[idx], ls[left_idx]):
        new_idx = left_idx
    else:
        new_idx = idx
    if right_idx < heap_size and comp(ls[new_idx], ls[right_idx]):
        new_idx = right_idx

    if new_idx != idx:
        swap(ls, idx, new_idx)
        bubble_down(ls, new_idx, heap_size, comp)
    else:
        return


def heap_sort(ls, comp=less):
    heap_size = len(ls)
    idx = heap_size // 2

    while idx >= 0:
        bubble_down(ls, idx, heap_size, comp)
        idx -= 1

    idx = heap_size
    while idx > 0:
        swap(ls, 0, heap_size - 1)
        heap_size -= 1
        bubble_down(ls, 0, heap_size, comp)
        idx -= 1
    return


def insertion_sort(ls, comp=less):
    if len(ls) < 2:
        return
    idx = 1
    while idx < len(ls):
        upper_idx = idx
        lower_idx = upper_idx - 1
        while lower_idx >= 0:
            if comp(ls[upper_idx], ls[lower_idx]):
                swap(ls, lower_idx, upper_idx)
                upper_idx -= 1
                lower_idx -= 1
            else:
                break
        idx += 1


def selection_sort(ls, comp=less):
    arr_len = len(ls)
    if arr_len < 2:
        return
    for idx in range(arr_len):
        min_element = ls[idx]
        temp = idx
        for item in range(idx, arr_len):
            if comp(ls[item], min_element):
                min_element = ls[item]
                temp = item
        swap(ls, idx, temp)
    return


def merge(ls, low, med, high, comp):
    # Merges ls[low: med + 1] with ls[med + 1: high + 1] i.e. up to and
    # including the endpoint

    left_len = med - low + 1
    right_len = high - med
    while left_len > 0 and right_len > 0:
        if not comp(ls[low], ls[med + 1]):
            temp = ls[med + 1]
            idx = med + 1
            while idx > low: # Shift terms in ls[low: med + 1] over to the right one unit
                ls[idx] = ls[idx - 1]
                idx -= 1
            ls[low] = temp
            right_len -= 1
            med += 1
        else:
            left_len -= 1
            low += 1
    return


def mergesort_helper(ls, low, high, comp=less):
    if low >= high:
        return ls

    mid = (high + low) // 2
    mergesort_helper(ls, low, mid, comp)
    mergesort_helper(ls, mid + 1, high, comp)
    merge(ls, low, mid, high, comp)

    return


def mergesort(ls, comp):
    mergesort_helper(ls, 0, len(ls) - 1, comp)
    return


def quicksort(ls, comp):
    pass


def main():
    inp = [4, 3, 1, 5, 6, 9, 4]
    heap_sort(inp, more)
    assert inp == sorted([4, 3, 1, 5, 6, 9, 4], reverse=True)

    inp = [5, 4, 3, 2, 1]
    heap_sort(inp, less)
    assert inp == sorted([5, 4, 3, 2, 1])

    inp = []
    sort(inp)
    assert inp == []

    inp = [4, 3, 1, 5, 6, 9, 4]
    insertion_sort(inp, more)
    assert inp == sorted([4, 3, 1, 5, 6, 9, 4], reverse=True)

    inp = [5, 4, 3, 2, 1]
    insertion_sort(inp, less)
    assert inp == sorted([5, 4, 3, 2, 1])

    inp = [1, 2, 3, 4, 5]
    sort(inp, kind="insertion")
    assert inp == sorted([1, 2, 3, 4, 5])

    inp = [4, 3, 1, 5, 6, 9, 4]
    selection_sort(inp, more)
    assert inp == sorted([4, 3, 1, 5, 6, 9, 4], reverse=True)

    inp = [5, 4, 3, 2, 1]
    selection_sort(inp, less)
    assert inp == sorted([5, 4, 3, 2, 1])

    inp = [1, 2, 3, 4, 5]
    sort(inp, kind="selection")
    assert inp == sorted([1, 2, 3, 4, 5])

    inp = [4, 3, 1, 5, 6, 9, 4]
    mergesort(inp, more)
    assert inp == sorted([4, 3, 1, 5, 6, 9, 4], reverse=True)

    inp = [5, 4, 3, 2, 1]
    mergesort(inp, less)
    assert inp == sorted([5, 4, 3, 2, 1])

    inp = [1, 2, 3, 4, 5]
    sort(inp, kind="merge")
    assert inp == sorted([1, 2, 3, 4, 5])

    # inp = [4, 3, 1, 5, 6, 9, 4]
    # quicksort(inp, more)
    # assert inp == sorted([4, 3, 1, 5, 6, 9, 4], reverse=True)
    #
    # inp = [5, 4, 3, 2, 1]
    # quicksort(inp, less)
    # assert inp == sorted([5, 4, 3, 2, 1])
    #
    # inp = [1, 2, 3, 4, 5]
    # sort(inp, kind="qsort")
    # assert inp == sorted([1, 2, 3, 4, 5])


if __name__ == "__main__":
    main()
