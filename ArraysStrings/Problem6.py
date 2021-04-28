# String compression: Compress a string on basis of character counts
# SO, e.g. aaabccaaaa --> a3b1c2a4. If the compressed string is not smaller
# than the original string, then the method should return the original string.


def compress(string):

    letter_list = []
    count_list = []
    idx = 0
    compressed = []

    while idx < len(string):
        letter = string[idx]
        count = 1
        idx += 1
        while idx < len(string) and string[idx] == letter:
            count += 1
            idx += 1
        compressed.append(letter + str(count))

    compressed = "".join(compressed)
    return compressed if len(compressed) < len(string) else string



def main():
    assert compress("aabccca") == "aabccca"
    assert compress("aaabccaaaa") == "a3b1c2a4"
    assert compress("b") == "b"
    assert compress("abc") == "abc"
    assert compress("abcc") == "abcc"
    assert compress("abccc") == "abccc"





if __name__ == "__main__":
    main()
    print("Problem 6")