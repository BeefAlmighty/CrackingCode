# URLify: replace all spaces in a string with %20.

def url(string):
    # without using .replace ...
    temp = string.strip()
    ans = []
    for char in temp:
        if char == " ":
            ans.append("%20")
        else:
            ans.append(char)
    return "".join(ans)

def main():
    assert url("Mr John Smith  ") == "Mr%20John%20Smith"
    assert url(" Nicholas  Hoell  ") == "Nicholas%20%20Hoell"
    assert url(" ") == ""
    assert url("") == ""
    assert url("nicholas") == "nicholas"

if __name__ == "__main__":
    main()
    print("Problem 3")