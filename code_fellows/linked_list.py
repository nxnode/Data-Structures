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
        current_node = self.head
        while current_node:
            count += 1
            current_node = current_node.next
        return count

    def search(self, value):
        if self.head == None:
            return None
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

    def display(self):
        list_output = []
        current_value = ""
        current_node = self.head
        while current_node:
            list_output.append(current_node.value)
            current_node = current_node.next
        list_output = list_output[::-1]
        return tuple(list_output)


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


if __name__ == "__main__":
    ll = LinkedList([3, "three"])
    ll_size = ll.size()
