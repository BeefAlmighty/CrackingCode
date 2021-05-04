# Write code to partition a linked list around an input such that
# all numbers smaller than the input are left of the rest.

from CrackingCode.LinkedLists.LinkedList import LinkedList

def partition(linked_list, pivot):
    # Idea: Iterate through the list moving any nodes that are less than
    # pivot to front of list.

    if len(linked_list) < 2:
        return

    stable = linked_list.head
    mover = linked_list.head.next

    while mover:
        if mover.item < pivot:
            stable.next = mover.next
            mover.next = linked_list.head
            linked_list.head = mover
            mover = stable.next
        else:
            stable = stable.next
            mover = mover.next

    return


def main():
    ll = LinkedList()


    ll.make_from_list([3, 5, 8, 5, 10, 2, 1])
    pivot = 5
    print("Before :", ll)
    partition(ll, pivot)
    print(f"After pivoting around {pivot}", ll)

    ll.make_from_list([3, 5, 8, 5, 10, 2, 1])
    pivot = 10
    print("Before :", ll)
    partition(ll, pivot)
    print(f"After pivoting around {pivot}", ll)

    ll.make_from_list([3, 5, 8, 5, 10, 2, 1])
    pivot = 3
    print("Before :", ll)
    partition(ll, pivot)
    print(f"After pivoting around {pivot}", ll)

    ll.make_from_list([3, 3, 3, 3])
    pivot = 31
    print("Before :", ll)
    partition(ll, pivot)
    print(f"After pivoting around {pivot}", ll)

    ll.make_from_list([3, 2, 1])
    pivot = 3
    print("Before :", ll)
    partition(ll, pivot)
    print(f"After pivoting around {pivot}", ll)


if __name__ == "__main__":
    main()
    print("Problem 4")