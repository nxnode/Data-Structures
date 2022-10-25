# https://codefellows.github.io/sea-python-401d6/assignments/linked_list.html

from code_fellows.linked_list import LinkedList


def test_linked_list():
    assert LinkedList(["head"]).head.value == "head"
    assert (
        LinkedList([3, "three"]).head.value == "head"
        and LinkedList([3, "three"]).head.next.value == 3
    )


def test_Linked_List_push():
    ll = LinkedList([3, "three"])
    assert ll.head.value == "three"
    assert ll.head.next.value == 3
    ll.push("new_head")
    assert ll.head.value == "new_head"
    assert ll.head.next.value == "three"
    assert ll.head.next.next.value == 3
