# https://codefellows.github.io/sea-python-401d6/assignments/linked_list.html

from code_fellows.linked_list import LinkedList, Node


def test_Linked_List():
    assert LinkedList(["head"]).head.value == "head"
    assert (
        LinkedList([3, "three"]).head.value == "head"
        and LinkedList([3, "three"]).head.next.value == 3
    )


def test_Linked_List_push():
    test_ll = LinkedList([999, 55, 1])
    assert test_ll.head.value == 1
    assert test_ll.head.next.value == 55
    assert test_ll.head.next.next.value == 999
    test_ll.push("newHead")
    assert test_ll.head.value == "newHead"
    assert test_ll.head.next.value == 1
    assert test_ll.head.next.next.value == 55
    assert test_ll.head.next.next.next.value == 999
