# Simple implementation of a LIFO stack

class Stack:
    def __init__(self, top=None):
        self._top = top  # Node at top of stack
        self._len = 0 if top is None else 1

    def __repr__(self):
        temp = self._top
        ans = ""
        while temp is not None:
            ans += "\n  | \n" + temp.__repr__()
            temp = temp.next()
        if ans: # Remove initial vertical bar
            ans = ans[5:]
        return ans

    def __len__(self):
        return self._len

    def pop(self):
        if self.isEmpty():
            print("Cannot pop from an empty stack!  Aborting.")
            return
        else:
            ans = self._top
            self._top = self._top.next()
            self._len -= 1
            return ans.get_item()

    def push(self, item):
        item = StackNode(item, self._top)
        self._top = item
        self._len += 1
        return None

    def peek(self):
        if self.isEmpty():
            print("Cannot run peek!  Aborting")
            return
        else:
            return self._top.get_item()

    def isEmpty(self):
        return self._top is None

    def make_from_list(self, ls):
        for item in ls:
            self.push(item)
        return


class StackNode:
    def __init__(self, item=None, next=None):
        self._item = item
        self._next = next

    def __repr__(self):
        return f"[ {self._item} ]"

    def get_item(self):
        return self._item

    def next(self):
        return self._next


def main():
    stack = Stack()
    stack.make_from_list([1, 2, 3, 4, 5])
    print(stack)
    assert len(stack) == 5

    assert stack.peek() == 5
    assert stack.pop() == 5
    print(stack)

    assert stack.peek() == 4
    assert len(stack) == 4

    stack.push(17)
    print(stack)
    assert stack.peek() == 17
    assert stack.pop() == 17

    stack.pop()
    print(stack)
    stack.pop()
    print(stack)
    stack.pop()
    print(stack)
    stack.pop()
    print(stack)
    stack.pop()
    print(stack)
    stack.pop()
    print(stack)
    stack.pop()

    assert len(stack) == 0

    stack.push(3.1415)
    print(stack)


if __name__ == "__main__":
    main()
    print("Done")