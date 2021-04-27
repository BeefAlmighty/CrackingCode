# Determine if a string has all unique characters.  Extra: what if you cannot
# use any additional data structures?


def uniqueEasy(string):
    temp = set()
    for char in string:
        if char in temp:
            return False
        else:
            temp.add(char)
    return True

def uniqueHard(string):
    if len(string) <= 1:
        return True
    temp = sorted(string)
    for idx in range(len(temp) - 1):
        if temp[idx] == temp[idx + 1]:
            return False
    return True



def main():
    assert uniqueEasy("nicholas") is True
    assert uniqueEasy("hoell") is False
    assert uniqueEasy("jackson191") is False
    assert uniqueEasy("1") is True
    assert uniqueEasy("") is True
    assert uniqueEasy("ll") is False
    assert uniqueEasy("  ") is False

    assert uniqueHard("nicholas") is True
    assert uniqueHard("hoell") is False
    assert uniqueHard("jackson191") is False
    assert uniqueHard("1") is True
    assert uniqueHard("") is True
    assert uniqueHard("ll") is False
    assert uniqueHard("  ") is False

if __name__ == "__main__":
    main()
