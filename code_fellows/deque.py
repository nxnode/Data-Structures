# https://codefellows.github.io/sea-python-401d6/assignments/deque.html


class Deque:
    def __init__(self):
        self.head = None
        self.tail = None
        self._length = 0

    def __len__(self):
        return self._length

    def size(self):
        return self._length

    def appendleft(self, value):
        node = Node(value)
        if self.head:
            node.next = self.head
            self.head.previous = node
        else:
            self.tail = node
        self.head = node
        self._length += 1

    def popleft(self):
        if self.head:
            popped_head = self.head
            self.head = self.head.next
            if self.head:
                self.head.previous = None
            self._length -= 1
            if len(self) <= 1:
                self.tail = self.head
            return popped_head.value
        else:
            raise ValueError("No head to pop")

    def peekleft(self):
        return self.head.value if self.head else None

    def append(self, value):
        node = Node(value)
        if self.tail:
            node.previous = self.tail
            self.tail.next = node
        else:
            self.head = node
        self.tail = node
        self._length += 1

    def pop(self):
        if self.tail:
            popped_tail = self.tail
            self.tail = self.tail.previous
            if self.tail:
                self.tail.next = None
            self._length -= 1
            if len(self) <= 1:
                self.head = self.tail
            return popped_tail.value
        else:
            raise ValueError("No tail to pop")

    def peek(self):
        return self.tail.value if self.tail else None


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None


if __name__ == "__main__":
    deq = Deque()
    deq.appendleft("head_next")
    deq.appendleft("head")
    deq.append("tail_prev")
    deq.append("tail")
