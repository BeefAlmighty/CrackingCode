# Sort an array of strings so that anagrams appear next to each other.

def swap(i, j, arr):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
    return

def is_anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    return sorted(s1) == sorted(s2)


def anagram_in_list(string, arr, pos):
    idx = 0
    while idx < len(arr):
        if is_anagram(string, arr[idx]):
            return idx + pos + 1
        idx += 1
    return False


def sort_anagrams(arr):
    for idx in range(len(arr) - 1):
        loc = anagram_in_list(arr[idx], arr[idx + 1:], idx)
        if loc is False:
            continue
        else:
            swap(idx + 1, loc, arr)



def main():
    ls = ["a", "ab", "d"]
    print("Before: ", ls)
    sort_anagrams(ls)
    print("After: ", ls)

    ls = ["a", "ab", "d", "ba"]
    print("\nBefore: ", ls)
    sort_anagrams(ls)
    print("After: ", ls)

    ls = ["a", "aba", "d", "ba"]
    print("\nBefore: ", ls)
    sort_anagrams(ls)
    print("After: ", ls)

    ls = ["a", "aba", "d", "baa"]
    print("\nBefore: ", ls)
    sort_anagrams(ls)
    print("After: ", ls)

    ls = ["a", "aba", "d", "baa", "aab"]
    print("\nBefore: ", ls)
    sort_anagrams(ls)
    print("After: ", ls)

if __name__ == "__main__":
    main()