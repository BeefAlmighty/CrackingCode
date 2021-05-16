# Simple implementation of a FIFO Queue

class Queue:
    def __init__(self, item=None):
        if item:
            self._front = QueueNode(item)
            self._len = 1
            self._back = self._front
        else:
            self._front = None
            self._len = 0
            self._back = None


    def __len__(self):
        return self._len

    def __repr__(self):
        if self.isEmpty():
            return ""
        else:
            ans = "[ back ] --> "
            temp = self._back
            while temp is not None:
                ans += f"[{temp.get_item()}] --> "
                temp = temp.next()
            ans = ans[:-5]
            ans += " <-- [ front ]"
            return ans

    def enqueue(self, item):
        if self._len == 0:
            self.__init__(item)
            return
        else:
            self._back = QueueNode(item, self._back)
            self._len += 1
            return

    def dequeue(self):
        if self.isEmpty():
            print("Cannot dequeue in an empty queue.  Aborting.\n")
            return
        elif self._front == self._back:
            ans = self.peek()
            self._front = None
            self._back = None
            self._len = 0
            return ans
        else:
            ans = self.peek()
            temp = self._back
            while temp.next() != self._front:
                temp = temp.next()
            self._front = temp
            temp._next = None
            self._len -= 1
            return ans

    def peek(self):
        if self.isEmpty():
            print("Cannot peek in an empty queue.  Aborting.\n")
            return
        else:
            return self._front.get_item()


    def isEmpty(self):
        return self._len == 0


class QueueNode:
    def __init__(self, item=None, next=None):
        self._item = item
        self._next = next

    def __repr__(self):
        return f" [{self._item}] "

    def __eq__(self, other):
        return self._item == other.get_item() and self._next == other.next()

    def get_item(self):
        return self._item

    def next(self):
        return self._next



def main():
    queue = Queue()
    assert len(queue) == 0
    queue.enqueue(17)
    print(queue)
    assert len(queue) == 1
    queue.enqueue(13)
    assert len(queue) == 2
    print(queue)
    assert queue.peek() == 17
    assert queue.dequeue() == 17
    print(queue)
    assert queue.dequeue() == 13
    print(queue)
    queue.dequeue()

    queue.enqueue(3.1415)
    queue.enqueue(2.71828)
    queue.enqueue(1.615)
    print(queue)
    queue.dequeue()
    print(queue.peek())
    print(queue)


if __name__ == "__main__":
    main()
    print("Queue")