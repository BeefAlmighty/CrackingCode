# Sparse search: Given a sorted array of strings interspersed with empty
# strings, return location of a given string.

def sparse_search(string_list, string, low=0, high=None):

    if high is None:
        high = len(string_list) - 1

    if low > high:
        return None

    while len(string_list[low]) == 0:
        low += 1
        if low > high:
            return None

    while len(string_list[high]) == 0:
        high -= 1

    mid = (low + high) // 2
    if string_list[mid] == string:
        return mid

    upper = mid
    lower = mid

    temp = string_list[upper]
    while upper >= low and temp == "":
        upper -= 1
        temp = string_list[upper]

    temp = string_list[lower]
    while lower < high and temp == "":
        lower += 1
        temp = string_list[lower]

    if string == string_list[upper]:
        return upper
    elif string == string_list[lower]:
        return lower
    elif string < string_list[upper]:
        return sparse_search(string_list, string, low, upper - 1)
    else:
        return sparse_search(string_list, string, lower + 1, high)





def main():
    string_list = ["at", "", "", "", "ball", "", "", "", "car"]
    assert sparse_search(string_list, "ball") == 4
    assert sparse_search(string_list, "at") == 0

    string_list = ["", "at", "", "", "", "ball", "", "", "", "car"]
    assert sparse_search(string_list, "ball") == 5
    assert sparse_search(string_list, "at") == 1
    assert sparse_search(string_list, "cat") is None

    string_list = ["a", "b", "cat"]
    assert sparse_search(string_list, "b")
    assert sparse_search(string_list, "cat")




if __name__ == "__main__":
    main()
    print("Problem 5")