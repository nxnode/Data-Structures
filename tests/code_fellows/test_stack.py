# https://codefellows.github.io/sea-python-401d6/assignments/stack.html

import pytest

from code_fellows.stack import Stack


def test_stack_push():
    stack = Stack([3, "three"])
    assert stack.linked_list.head.value == "three"
    assert stack.linked_list.head.next.value == 3
    stack.push("new_head")
    assert stack.linked_list.head.value == "new_head"
    assert stack.linked_list.head.next.value == "three"
    assert stack.linked_list.head.next.next.value == 3
    stack = Stack()
    stack.push("new_head")
    assert stack.linked_list.head.value == "new_head"


def test_stack_pop_and_len_():
    stack = Stack([3, "three", "nine"])
    assert len(stack) == 3
    expected = stack.linked_list.head
    assert stack.linked_list.pop() == expected
    assert stack.linked_list.head.value == "three"
    assert len(stack) == 2
    stack = Stack()
    with pytest.raises(ValueError) as ex:
        stack.pop()
    assert str(ex.value) == "Empty list try again"
    assert stack.linked_list._length == 0
    assert len(stack) == 0
