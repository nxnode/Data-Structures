# https://codefellows.github.io/sea-python-401d6/assignments/linked_list.html

import pytest
import sys
from code_fellows.linked_list import LinkedList
from io import StringIO


def test_linked_list():
    assert LinkedList([3, "three"]).head.value == "three"
    assert LinkedList([3, "three"]).head.next.value == 3
    assert LinkedList().head == None
    assert LinkedList((3, "three", "nine")).head.value == "nine"
    assert LinkedList((3, "three", "nine")).head.next.value == "three"


def test_linked_list_push():
    ll = LinkedList([3, "three"])
    assert ll.head.value == "three"
    assert ll.head.next.value == 3
    ll.push("new_head")
    assert ll.head.value == "new_head"
    assert ll.head.next.value == "three"
    assert ll.head.next.next.value == 3
    ll = LinkedList()
    ll.push("new_head")
    assert ll.head.value == "new_head"


def test_linked_list_size_and_len():
    ll = LinkedList([3, "three"])
    assert ll.size() == 2
    ll = LinkedList(["new_head", 3, "three"])
    assert ll.size() == 3
    assert len(ll) == 3
    ll.push(9)
    assert ll.size() == 4
    assert len(ll) == 4
    ll.pop()
    assert ll.size() == 3
    assert len(ll) == 3
    ll = LinkedList()
    assert ll.size() == 0
    assert len(ll) == 0


def test_linked_list_search():
    ll = LinkedList([3, "three", "nine"])
    assert ll.search(3).value == 3
    expected = ll.head.next.next
    assert ll.search(3) == expected
    ll = LinkedList()
    assert ll.search(3) == None


def test_linked_list_pop_correct_size_and_len_is_maintained():
    ll = LinkedList([3, "three", "nine"])
    assert ll.size() == 3
    assert len(ll) == 3
    expected = ll.head
    assert ll.pop() == expected
    assert ll.head.value == "three"
    assert ll.size() == 2
    assert len(ll) == 2
    ll = LinkedList()
    with pytest.raises(ValueError) as ex:
        ll.pop()
    assert str(ex.value) == "Empty list try again"
    assert ll._length == 0
    assert len(ll) == 0


def test_display():
    ll = LinkedList([3, "three", "nine"])
    assert ll.display() == "(3, 'three', 'nine')"


def test__print__():
    ll = LinkedList([3, "three", "nine"])
    buffer = StringIO()
    sys.stdout = buffer
    print(ll)
    print_output = buffer.getvalue()
    sys.stdout = sys.__stdout__
    assert print_output == "(3, 'three', 'nine')"
