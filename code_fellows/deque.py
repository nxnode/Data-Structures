# https://codefellows.github.io/sea-python-401d6/assignments/deque.html

# Deque features:

# append(val): adds value to the end of the deque
# appendleft(val): adds a value to the front of the deque
# pop(): removes a value from the end of the deque and returns it (raises an exception if the deque is empty)
# popleft(): removes a value from the front of the deque and returns it (raises an exception if the deque is empty)
# peek(): returns the next value that would be returned by pop but leaves the value in the deque (returns None if the deque is empty)
# peekleft(): returns the next value that would be returned by popleft but leaves the value in the deque (returns None if the deque is empty)
# size(): returns the count of items in the queue (returns 0 if the queue is empty)


class Deque:
    def __init__(self, value=None):
        self.head = None
        self.tail = None
        self._length = 0

    def __len__(self):
        return self._length

    def size(self):
        return self._length

    def append(self, value):
        node = Node(value)
        node.previous = self.tail
        if self.tail:
            self.tail.next = node
        else:
            self.head = node
        self.tail = node
        self._length += 1

    def appendleft(self, value):
        node = Node(value)
        node.next = self.head
        if self.head:
            self.head.previous = node
        else:
            self.tail = node
        self.head = node
        self._length += 1

    def popleft(self):
        popped_head = self.head
        if self.head:
            old_head_next = self.head.next
            self.head = old_head_next
            self._length -= 1
            if self._length == 1:
                self.tail = self.head
            if self._length == 0:
                self.head = self.tail
            return popped_head.value
        else:
            raise ValueError("No head to pop")

    def peekleft(self):
        popped_head = self.head
        if self._length == 0:
            return None
        if self.head:
            return popped_head.value
        else:
            return None

    def pop(self):
        popped_tail = self.tail
        if self.tail:
            old_tail_prev = self.tail.previous
            self.tail = old_tail_prev
            self._length -= 1
            if self._length == 1:
                self.head = self.tail
            if self._length == 0:
                self.head, self.tail = None, None
            return popped_tail.value

        else:
            raise ValueError("No tail to pop")

    def peek(self):
        if self._length == 0:
            return None
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
