# Write code to remove duplicates from unsorted linked list
# Bonus: What if temporary buffer was not allowed?

from CrackingCode.LinkedLists.LinkedList import LinkedList, Node

def remove_node(node, linked_list):
    """
    Remove Node node from given linked list

    :param node: CrackingCode.LinkedLists.LinkedList.Node
    :param linked_list: CrackingCode.LinkedLists.LinkedList.LinkedList
    :return: None
    """

    if node == linked_list.head:
        linked_list.head = linked_list.head.next
        return

    temp = linked_list.head
    while temp.next:
        if temp.next == node:
            temp.next = temp.next.next
            return
        else:
            temp = temp.next
    return


def remove_duplicates_buffer(linked_list):
    buff = {}
    temp = linked_list.head
    while temp:
        if temp.item in buff:
            buff[temp.item] += 1
        else:
            buff[temp.item] = 1
        temp = temp.next

    temp = linked_list.head
    while temp.next is not None:
        if buff[temp.item] > 1:
            remove_node(temp, linked_list)
            buff[temp.item] -= 1
        temp = temp.next

    return


def remove_duplicates(linked_list):
    # Idea is as follows : Beginning with head of the list,
    # move through the list and remove any node that matches the head item
    # then apply this process to head's next node.

    if linked_list.head.next is None:
        return

    front = linked_list.head
    runner = linked_list.head

    while front.next:
        if runner.next is not None:
            runner = runner.next
            if runner.item == front.item:
                remove_node(runner, linked_list)
                runner = front
        else:
            front = front.next
            runner = front

    return



def main():

    node = Node(3.14)
    node1 = Node(2.718, node)
    head = Node(1.615, node1)

    linked_list = LinkedList(head)
    print(linked_list)
    remove_node(node, linked_list)
    print(linked_list)
    remove_node(head, linked_list)
    print(linked_list)

    linked_list = LinkedList()

    linked_list.make_from_list([2, 3, 4, 5])
    print("Before : ", linked_list)
    remove_duplicates_buffer(linked_list)
    print("After : ", linked_list)
    linked_list.make_from_list([2, 3, 4, 5])
    print("Before : ", linked_list)
    remove_duplicates_buffer(linked_list)
    remove_duplicates(linked_list)
    print("After No Buffer: ", linked_list)

    linked_list.make_from_list([2, 3, 4, 2])
    print("Before : ", linked_list)
    remove_duplicates_buffer(linked_list)
    print("After : ", linked_list)
    linked_list.make_from_list([2, 3, 4, 2])
    print("Before : ", linked_list)
    remove_duplicates_buffer(linked_list)
    remove_duplicates(linked_list)
    print("After No Buffer: ", linked_list)

    linked_list.make_from_list([2, 2, 2, 2])
    print("Before : ", linked_list)
    remove_duplicates_buffer(linked_list)
    print("After : ", linked_list)
    linked_list.make_from_list([2, 2, 2, 2])
    print("Before : ", linked_list)
    remove_duplicates_buffer(linked_list)
    remove_duplicates(linked_list)
    print("After No Buffer: ", linked_list)

    linked_list.make_from_list([2, 3, 2, 3])
    print("Before : ", linked_list)
    remove_duplicates_buffer(linked_list)
    print("After : ", linked_list)
    linked_list.make_from_list([2, 3, 2, 3])
    print("Before : ", linked_list)
    remove_duplicates_buffer(linked_list)
    remove_duplicates(linked_list)
    print("After No Buffer: ", linked_list)

    linked_list.make_from_list([12, 3, -4, 15, -4])
    print("Before : ", linked_list)
    remove_duplicates_buffer(linked_list)
    print("After : ", linked_list)
    linked_list.make_from_list([12, 3, -4, 15, -4])
    print("Before : ", linked_list)
    remove_duplicates_buffer(linked_list)
    remove_duplicates(linked_list)
    print("After No Buffer: ", linked_list)

    linked_list.make_from_list([12])
    print("Before : ", linked_list)
    remove_duplicates_buffer(linked_list)
    print("After : ", linked_list)
    linked_list.make_from_list([12])
    print("Before : ", linked_list)
    remove_duplicates_buffer(linked_list)
    remove_duplicates(linked_list)
    print("After No Buffer: ", linked_list)


if __name__ == "__main__":
    main()
    print("Problem 1")
