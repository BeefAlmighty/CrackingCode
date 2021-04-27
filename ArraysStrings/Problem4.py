# Determine is a string is a permutation of a palindrome.
# NB: I assume case insensitivity

def isPalPerm(string):
    char_dict = {}
    num_odd = 0
    for char in string.lower():
        if char == " ":
            continue
        elif char not in char_dict:
            char_dict[char] = True
            num_odd += 1
        else:
            char_dict[char] = not char_dict[char]
            if char_dict[char]:
                num_odd += 1
            else:
                num_odd -= 1
    return num_odd < 2




def main():
    assert isPalPerm("") is True
    assert isPalPerm("Nicholas") is False
    assert isPalPerm("Tact Coa") is True
    assert isPalPerm(" Taco cat   ") is True
    assert isPalPerm(" ") is True



if __name__ == "__main__":
    main()
    print("Problem 4")