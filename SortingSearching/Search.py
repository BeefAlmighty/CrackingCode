

def binary_search(arr, item, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    if low > high:
        return None
    med = (low + high) // 2
    if arr[med] == item:
        return med
    elif arr[med] > item:
        return binary_search(arr, item, low, med - 1)
    else:
        return binary_search(arr, item, med + 1, high)


def main():
    arr = [4, 6, 8, 9, 12, 13]
    assert binary_search(arr, 4) == 0
    assert binary_search(arr, 13) == 5
    assert binary_search(arr, 9) == 3
    assert binary_search(arr, -1) is None





if __name__ == "__main__":
    main()