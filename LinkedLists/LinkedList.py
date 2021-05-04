# Implementation of linked list data structure

class LinkedList:

    def __init__(self, node=None):
        self.head = node

    def __repr__(self):
        temp = self.head
        ans = temp.__repr__()
        while temp.next:
            temp = temp.next
            ans += " --> " + temp.__repr__()
        ans += " --> [ X ]"
        return ans

    def __eq__(self, other):
        temp = self.head
        temp_2 = other.head
        while temp and temp_2:
            if temp != temp_2:
                return False
            temp = temp.next
            temp_2 = temp_2.next
        if temp is None and temp_2 is not None:
            return False
        elif temp is not None and temp_2 is None:
            return False
        else:
            return True

    def make_from_list(self, ls):
        """
        Helper for doing testing, makes a singly linked list object from
        a List object
        :param ls: List
        :return: self
        """

        self.head = Node(ls[0])
        temp = self.head
        idx = 1

        while idx < len(ls):
            temp.next = Node(ls[idx])
            idx += 1
            temp = temp.next

        return

    def __len__(self):
        temp = self.head
        ans = 0
        while temp:
            ans += 1
            temp = temp.next
        return ans


class Node:
    def __init__(self, item, next=None, prev=None):
        self.item = item
        self.next = next
        self.prev = prev

    def __repr__(self):
        return f"[ {self.item} ]"

    def __eq__(self, other):
        return self.item == other.item and self.next == other.next



def main():
    node = Node(3.14)
    print(node)

    node = Node(2.718, node)
    head = Node(1.615, node)

    linked_list = LinkedList(head)
    print(linked_list)

    linked_list = LinkedList()
    linked_list.make_from_list([1, 2, 3])
    print(linked_list)

    print(len(linked_list))

if __name__ == "__main__":
    main()