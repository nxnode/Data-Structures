# https://codefellows.github.io/sea-python-401d6/assignments/stack.html

from code_fellows.linked_list import LinkedList


class Stack(LinkedList):
    def pop(self):
        try:
            return super().pop().value
        except ValueError:
            raise ValueError("Empty Stack")


if __name__ == "__main__":
    stack_var = Stack([3, 4, 5])
    print(len(stack_var))
    for i in range(4):
        print(stack_var.pop())
