# https://codefellows.github.io/sea-python-401d6/assignments/binary_heap.html


class Heap:
    def __init__(self, values=None):
        self._length = 0
        self.size = 0
        self.root = None
        if values:
            pass

    def push(self, value):
        pass

    def pop(self):
        pass


class Node:
    def __init__(self, value):
        self.value = value
        self.child_left = None
        self.child_right = None
        self.parent = None
