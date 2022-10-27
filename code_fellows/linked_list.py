# https://codefellows.github.io/sea-python-401d6/assignments/linked_list.html


class LinkedList:
    def __init__(self, values=None):
        self.head = None
        if values:
            for value in values:
                self.head = Node(value, next=self.head)

    def push(self, value):
        self.head = Node(value, next=self.head)

    def size(self):
        count = 0
        currrent_node = self.head
        while currrent_node:
            count += 1
            currrent_node = currrent_node.next
        return count

    def search(self, value):
        count = 1
        current_node = self.head
        while value != current_node.value:
            count += 1
            current_node = current_node.next
        if value == current_node.value:
            return current_node
        else:
            return None

    def pop(self):
        try:
            head_pop = self.head
            self.head = self.head.next
            return head_pop
        except AttributeError:
            raise ValueError("Empty list try again")


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


if __name__ == "__main__":
    ll = LinkedList([3, "three"])
    ll_size = ll.size()
