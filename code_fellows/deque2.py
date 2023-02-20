# https://codefellows.github.io/sea-python-401d6/assignments/deque.html

from code_fellows.doubly_linked_list import DLL


class Deque:
    def __init__(self):
        self.storage = DLL()

    def __len__(self):
        return len(self.storage)

    def size(self):
        return len(self)

    def appendleft(self, value):
        self.storage.push(value)

    def popleft(self):
        try:
            return self.storage.pop()
        except ValueError:
            raise ValueError("No head to pop")

    def peekleft(self):
        return self.storage.head.value if self.storage.head else None

    def append(self, value):
        self.storage.append(value)

    def pop(self):
        try:
            return self.storage.shift()
        except ValueError:
            raise ValueError("No tail to pop")

    def peek(self):
        return self.storage.tail.value if self.storage.tail else None
