# https://codefellows.github.io/sea-python-401d6/assignments/deque.html


class Deque:
    def __init__(self, value=None):
        self.head = None
        self.tail = None
        self._length = 0

    def __len__(self):
        return self._length

    def size(self):
        return self._length

    # HEAD
    def appendleft(self, value):
        node = Node(value)
        node.next = self.head
        if self.head:
            self.head.previous = node
        else:
            self.tail = node
        self.head = node
        self._length += 1

    # HEAD
    def popleft(self):
        popped_head = self.head
        if self.head:
            self.head = self.head.next
            self._length -= 1
            return popped_head.value
        else:
            raise ValueError("No head to pop")

    # HEAD
    def peekleft(self):
        popped_head = self.head
        if self.head:
            return popped_head.value
        else:
            return None

    # TAIL
    def append(self, value):
        node = Node(value)
        node.previous = self.tail
        if self.tail:
            self.tail.next = node
        else:
            self.head = node
        self.tail = node
        self._length += 1

    # TAIL
    def pop(self):
        popped_tail = self.tail
        if self.tail:
            old_tail_prev = self.tail.previous
            self.tail = old_tail_prev
            self._length -= 1
            return popped_tail.value
        else:
            raise ValueError("No tail to pop")

    # TAIL
    def peek(self):
        popped_tail = self.tail
        if self.tail:
            return popped_tail.value
        else:
            return None


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None


if __name__ == "__main__":
    deq = Deque()
    deq.append("tail")
    deq.appendleft("head")
