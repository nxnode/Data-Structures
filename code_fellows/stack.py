# https://codefellows.github.io/sea-python-401d6/assignments/stack.html

from code_fellows.linked_list import LinkedList


class Stack:
    def __init__(self, values=None):
        self.linked_list = LinkedList(values)

    def push(self, value):
        self.linked_list.push(value)

    def pop(self):
        try:
            return self.linked_list.pop()
        except ValueError:
            raise ValueError("Empty Stack try again")

    def __len__(self):
        return len(self.linked_list)


if __name__ == "__main__":
    print(len(Stack()))
