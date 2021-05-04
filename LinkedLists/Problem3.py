# Delete the middle node.  Given only access to a node in middle of a singly
# linked list, remove that node from the list.

from CrackingCode.LinkedLists.LinkedList import LinkedList, Node

def remove_middle(node, linked_list):
    temp = linked_list.head
    while temp.next != node:
        temp = temp.next
    temp.next = temp.next.next
    return



def main():
    end = Node(3.14)
    end = Node(2.71828, end)
    mid = Node("c", end)
    front = Node("b", mid)
    front = Node("a", front)
    ll = LinkedList(front)
    print("Before : ", ll)
    remove_middle(mid, ll)
    print("After : ", ll)


if __name__ == "__main__":
    main()
    print("Problem 3")