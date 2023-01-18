# https://codefellows.github.io/sea-python-401d6/assignments/stack.html


class Stack:
    def __init__(self, values=None):
        self.head = None
        self._length = 0
        if values:
            for value in values:
                self.head = Node(value, next=self.head)
                self._length += 1

    def __len__(self):
        return self._length

    def push(self, value):
        self.head = Node(value, next=self.head)
        self._length += 1

    def pop(self):
        try:
            head_pop = self.head
            self.head = self.head.next
            self._length -= 1
            return head_pop
        except AttributeError:
            raise ValueError("Empty stack, try again")


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


if __name__ == "__main__":
    stack_test = Stack(3)
    stack_test = Stack("three")
    stack_test = Stack("nine")
