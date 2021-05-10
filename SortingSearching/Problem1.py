# Sorted merge.  Given A and B, which are sorted arrays, merge B into A sorted.

def sorted_merge(arr1, arr2):
    front1 = 0
    front2 = 0

    if not arr2:
        return

    back = 0
    while arr1[back]:
        back += 1

    while front1 < back and front2 < len(arr2):
        if arr2[front2] >= arr1[front1]:
            front1 += 1
            continue
        temp = back
        while temp > front1:
            arr1[temp] = arr1[temp - 1]
            temp -= 1
        arr1[temp] = arr2[front2]
        front2 += 1
        back += 1

    while front2 < len(arr2):
        arr1[back] = arr2[front2]
        back += 1
        front2 += 1

    return




def main():
    arr1 = [1, 2, 3, None, None, None]
    arr2 = [1, 2, 5]
    sorted_merge(arr1, arr2)

    assert arr1 == [1, 1, 2, 2, 3, 5]

    arr1 = [1, 2, 3, None, None, None]
    arr2 = []
    sorted_merge(arr1, arr2)
    assert arr1 == [1, 2, 3, None, None, None]

    arr1 = [1, 2, 3, None, None, None]
    arr2 = [1, 2, 3]
    sorted_merge(arr1, arr2)
    assert arr1 == [1,1, 2, 2, 3, 3]

    arr1 = [1, 12, 30, None]
    arr2 = [17]
    sorted_merge(arr1, arr2)
    assert arr1 == [1, 12, 17, 30]

    arr1 = [1, 12, 30, None, None]
    arr2 = [0, 9]
    sorted_merge(arr1, arr2)
    assert arr1 == [0, 1, 9, 12,  30]


if __name__ == "__main__":
    main()