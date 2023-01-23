# https://codefellows.github.io/sea-python-401d6/assignments/doubly_linked_list.html


class DLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self._iter_next = None
        self._length = 0

    def push(self, value):
        node = Node(value)
        node.next = self.head
        if self.head:
            self.head.previous = node
        else:
            self.tail = node
        self.head = node
        self._length += 1

    def append(self, value):
        node = Node(value)
        node.previous = self.tail
        if self.tail:
            self.tail.next = node
        else:
            self.head = node
        self.tail = node
        self._length += 1

    def __iter__(self):
        self._iter_next = self.head
        return self

    def __next__(self):
        if self._iter_next:
            iter_next = self._iter_next
            self._iter_next = self._iter_next.next
            return iter_next
        raise StopIteration

    def remove(self, value):
        found = False
        for node in self:
            if node.value == value:
                found = True
                self._length -= 1
                if node.previous:
                    node.previous.next = node.next
                else:
                    self.head = node.next
                if node.next:
                    node.next.previous = node.previous
                else:
                    self.tail = node.previous
        if not found:
            raise ValueError("Not found")

    def shift(self):
        shifted_tail = self.tail
        if self.tail:
            old_tail_prev = self.tail.previous
            self.tail = old_tail_prev
            self._length -= 1
            return shifted_tail.value
        else:
            raise ValueError("No tail to shift")

    def pop(self):
        shifted_head = self.head
        if self.head:
            self.head = self.head.next
            self._length -= 1
            return shifted_head.value
        else:
            raise ValueError("No head to pop")


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None


if __name__ == "__main__":
    doublyll = DLL()
    doublyll.push("three")
    doublyll.push("five")
    doublyll.push("another")
