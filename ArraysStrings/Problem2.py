# Given 2 strings, check if one is a permutation of the other.

def isPermutation(s1, s2):
    if len(s1) != len(s2):
        return False
    return sorted(s1) == sorted(s2)



def main():
    assert isPermutation("hello", "hoell") is True
    assert isPermutation("hello", "Hoell") is False
    assert isPermutation("hello", "here") is False
    assert isPermutation("hoell", "hello") is True
    assert isPermutation("nicholas", "sandwich") is False
    assert isPermutation("", "nicholas") is False
    assert isPermutation("nicholas", "olashcin") is True

if __name__ == "__main__":
    main()
    print("Problem 2")