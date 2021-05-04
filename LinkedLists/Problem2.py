# Return kth to last element in a linked list

from CrackingCode.LinkedLists.LinkedList import LinkedList

def kth_last(linked_list, k):
    length = len(linked_list)
    count = 1
    temp = linked_list.head
    while count < length - k:
        count += 1
        temp = temp.next
    return temp.item


def main():
    linked_list = LinkedList()

    linked_list.make_from_list([2, 3, 4, 5])
    assert kth_last(linked_list, 0) == 5
    assert kth_last(linked_list, 1) == 4
    assert kth_last(linked_list, 2) == 3
    assert kth_last(linked_list, 3) == 2



if __name__ == "__main__":
    main()
    print("Problem 2")