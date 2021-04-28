# One away: there are 3 basic edits to make on strings.  Replacing a character,
# inserting a character, deleting a character.  Write a function to take in
# 2 strings and determine if they are at most 1 edit away from each other.

def insert(s1, s2):
    """
    s1 is the longer of the 2 strings
    :param s1: string
    :param s2: string
    :return: bool
    """
    for idx in range(len(s2)):
        if s1[idx] == s2[idx]:
            continue
        else:
            return s1[idx + 1:] == s2[idx:]
    return True

def replace(s1, s2):
    diff = 0
    for idx in range(len(s1)):
        if s1[idx] == s2[idx]:
            continue
        else:
            diff += 1
            if diff > 1:
                return False
    return True

def one_away(s1, s2):

    s1_len = len(s1)
    s2_len = len(s2)

    if abs(s1_len - s2_len) > 1:
        return False
    elif s1 == s2:
        return True
    elif s1_len == s2_len:
        return replace(s1, s2)
    else:
        return insert(s1, s2) if s1_len > s2_len else insert(s2, s1)


def main():
    assert one_away("pale", "ple") is True
    assert one_away("ple", "pale") is True
    assert one_away("pales", "pale") is True
    assert one_away("pale", "bale") is True
    assert one_away("bake", "pale") is False
    assert one_away("hoell", "hoell") is True
    assert one_away("", " ") is True
    assert one_away("", "  ") is False
    assert one_away("hoell", "hoell ") is True
    assert one_away(" hoell", "hoell ") is False
    assert one_away("x", "") is True



if __name__ == "__main__":
    main()
    print("Problem 5")