# https://codefellows.github.io/sea-python-401d6/assignments/linked_list.html

import pytest

from code_fellows.linked_list import LinkedList


def test_linked_list():
    assert LinkedList([3, "three"]).head.value == "three"
    assert LinkedList([3, "three"]).head.next.value == 3
    assert LinkedList().head == None


def test_Linked_List_push():
    ll = LinkedList([3, "three"])
    assert ll.head.value == "three"
    assert ll.head.next.value == 3
    ll.push("new_head")
    assert ll.head.value == "new_head"
    assert ll.head.next.value == "three"
    assert ll.head.next.next.value == 3


def test_Linked_List_size():
    ll = LinkedList([3, "three"])
    assert ll.size() == 2
    ll = LinkedList(["new_head", 3, "three"])
    assert ll.size() == 3
    ll.push(9)
    assert ll.size() == 4
    ll.pop()
    assert ll.size() == 3


def test_Linked_List_search():
    ll = LinkedList([3, "three", "nine"])
    assert ll.search(3).value == 3
    expected = ll.head.next.next
    assert ll.search(3) == expected


def test_linked_list_pop_correct_size_is_maintained():
    ll = LinkedList([3, "three", "nine"])
    assert ll.size() == 3
    expected = ll.head
    assert ll.pop() == expected
    assert ll.head.value == "three"
    assert ll.size() == 2
    ll = LinkedList()
    with pytest.raises(ValueError) as ex:
        ll.pop()
    assert str(ex.value) == "Empty list try again"
