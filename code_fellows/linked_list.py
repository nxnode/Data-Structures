# https://codefellows.github.io/sea-python-401d6/assignments/linked_list.html


class LinkedList:
    def __init__(self, values=None):
        self.head = None
        if values:
            for value in values:
                self.head = Node(value, next=self.head)

    def push(self, value):
        self.head = Node(value, next.self.head)


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
