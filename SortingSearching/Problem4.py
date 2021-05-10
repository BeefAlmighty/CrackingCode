# A Data Structure called Listy lacks a size method but does have
# an elementAt() method which returns -1 if input exceeds the size.
# Listy only comtains positive integers.  If a Listy contains sorted
# positive integers find index of given input.


class Listy:
    def __init__(self, ls=None):
        self._ls = ls

    def elementAt(self, i):
        if i > len(self._ls) - 1:
            return -1
        else:
            return self._ls[i]


def find_index(listy, item, low=0, high=1):
    if listy.elementAt(low) > item:
        return None
    elif item == listy.elementAt(low):
        return low
    elif item == listy.elementAt(high):
        return high
    elif low >= high:
        return None
    elif listy.elementAt(high) == -1:
        return find_index(listy, item, low, high // 2 + 1)
    elif item > listy.elementAt(high):
        return find_index(listy, item, high + 1, 2 * high + 1)
    else:
        medium = (low + high) // 2
        medium_val = listy.elementAt(medium)
        if item == medium_val:
            return medium
        elif item < medium_val:
            return find_index(listy, item, low + 1, medium_val - 1)
        else:
            return find_index(listy, item, medium_val + 1, high - 1)


def main():
    ls = [12, 14, 14, 14, 16, 21, 33, 34]
    listy = Listy(ls)
    nums = [14, 13, 34, 35]
    print("Listy: ", ls)
    for num in nums:
        print(f"find index of {num}: ", find_index(listy, num))

    ls = [1, 1, 1, 1, 3, 4, 4, 4, 4, 4]
    listy = Listy(ls)
    nums = [14, 13, 1, -1, 4]
    print("Listy: ", ls)
    for num in nums:
        print(f"find index of {num}: ", find_index(listy, num))


if __name__ == "__main__":
    main()
    print("Problem 4")
