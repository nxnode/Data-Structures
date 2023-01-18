# https://codefellows.github.io/sea-python-401d6/assignments/stack.html

import pytest

from code_fellows.stack import Stack


def test_stack_push():
    stack = Stack()
    stack.push("three")
    stack.push("two")
    assert stack.head.value == "two"
    assert stack.head.next.value == "three"
    stack.push("one")
    assert stack.head.value == "one"
    assert stack.head.next.value == "two"
    assert stack.head.next.next.value == "three"
    stack = Stack()
    stack.push("new_head")
    assert stack.head.value == "new_head"


def test_stack_pop_and_len_():
    stack = Stack()
    stack.push("three")
    stack.push("two")
    stack.push("one")
    assert len(stack) == 3
    assert stack.pop().value == "one"
    assert stack.head.value == "two"
    assert len(stack) == 2
    stack = Stack()
    with pytest.raises(ValueError) as ex:
        stack.pop()
    assert str(ex.value) == "Empty stack, try again"
    assert len(stack) == 0
