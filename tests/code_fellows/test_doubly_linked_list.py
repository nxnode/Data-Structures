# https://codefellows.github.io/sea-python-401d6/assignments/doubly_linked_list.html

import pytest

from code_fellows.doubly_linked_list import DLL


def test_linked_list():
    doublyll = DLL()
    doublyll.push("three")
    doublyll.push("five")
    doublyll.push("seven")
    assert doublyll.head.value == "seven"
    assert doublyll.head.next.previous.value == "seven"
    assert doublyll.head.previous == None
    assert doublyll.head.next.value == "five"
    assert doublyll.head.next.next.value == "three"
    assert doublyll.tail.value == "three"
    assert doublyll.tail.previous.value == "five"


def test_append_and_length():
    doublyll = DLL()
    assert doublyll._length == 0
    doublyll.append("three")
    assert doublyll._length == 1
    doublyll.append("five")
    assert doublyll._length == 2
    doublyll.append("seven")
    assert doublyll._length == 3
    assert doublyll.tail.value == "seven"
    assert doublyll.tail.previous.next.value == "seven"
    assert doublyll.tail.next == None
    assert doublyll.tail.previous.value == "five"
    assert doublyll.tail.previous.previous.value == "three"
    assert doublyll.head.value == "three"
    assert doublyll.head.next.value == "five"


def test__iter__():
    doublyll = DLL()
    # with pytest.raises(StopIteration):
    values = [node.value for node in doublyll]
    assert not values
    doublyll.push("another")
    values = [node.value for node in doublyll]
    assert values == ["another"]


def test_remove():
    doublyll = DLL()
    doublyll.append("three")
    doublyll.append("five")
    doublyll.append("seven")
    doublyll.remove("five")
    assert doublyll.tail.value == "seven"
    assert doublyll.tail.previous.next.value == "seven"
    assert doublyll.tail.next == None
    assert doublyll.tail.previous.value == "three"
    assert doublyll.head.value == "three"
    assert doublyll.head.next.value == "seven"
    doublyll.remove("seven")
    assert doublyll.head.value == "three"
    assert doublyll.head.next == None
    assert doublyll.tail.value == "three"
    assert doublyll.tail.previous == None
    doublyll.remove("three")
    assert doublyll.head == None
    assert doublyll.tail == None
    doublyll.push("eight")
    doublyll.push("nine")
    assert doublyll.head.value == "nine"
    doublyll.remove("nine")
    assert doublyll.head.value == "eight"
    assert doublyll.tail.value == "eight"
    assert doublyll.head.next == None
    assert doublyll.head.previous == None
    with pytest.raises(ValueError) as error:
        doublyll.remove("nope")
    assert str(error.value) == "Not found"


def test_shift():
    doublyll = DLL()
    doublyll.append("1")
    doublyll.append("2")
    doublyll.append("3")
    doublyll.append("4")
    assert doublyll.tail.value == "4"
    assert doublyll.tail.previous.next.value == "4"
    assert doublyll.tail.next == None
    assert doublyll.tail.previous.value == "3"
    assert doublyll.head.value == "1"
    assert doublyll.head.next.value == "2"
    assert doublyll.shift() == "4"
    assert doublyll.head.value == "1"
    assert doublyll.head.next.value == "2"
    assert doublyll.tail.value == "3"
    assert doublyll.tail.previous.value == "2"
    assert doublyll.tail.previous.next.value == "3"
    assert doublyll.shift() == "3"
    assert doublyll.head.value == "1"
    assert doublyll.head.next.value == "2"
    assert doublyll.tail.value == "2"
    assert doublyll.tail.previous.value == "1"
    assert doublyll.tail.previous.next.value == "2"
    assert doublyll.shift() == "2"
    assert doublyll.shift() == "1"
    with pytest.raises(ValueError) as error:
        doublyll.shift()
    assert str(error.value) == "No tail to shift"
    with pytest.raises(ValueError) as error:
        doublyll = DLL()
        doublyll.shift()
    assert str(error.value) == "No tail to shift"


def test_pop_and_length():
    doublyll = DLL()
    doublyll.append("1")
    doublyll.append("2")
    doublyll.append("3")
    doublyll.append("4")
    assert doublyll._length == 4
    assert doublyll.tail.value == "4"
    assert doublyll.tail.previous.next.value == "4"
    assert doublyll.tail.next == None
    assert doublyll.tail.previous.value == "3"
    assert doublyll.head.value == "1"
    assert doublyll.head.next.value == "2"
    assert doublyll.pop() == "1"
    assert doublyll._length == 3
    assert doublyll.head.value == "2"
    assert doublyll.head.next.value == "3"
    assert doublyll.tail.value == "4"
    assert doublyll.tail.previous.value == "3"
    assert doublyll.tail.previous.next.value == "4"
    assert doublyll.pop() == "2"
    assert doublyll._length == 2
    assert doublyll.head.value == "3"
    assert doublyll.head.next.value == "4"
    assert doublyll.tail.value == "4"
    assert doublyll.tail.previous.value == "3"
    assert doublyll.tail.previous.next.value == "4"
    assert doublyll.pop() == "3"
    assert doublyll._length == 1
    assert doublyll.pop() == "4"
    assert doublyll._length == 0
    with pytest.raises(ValueError) as error:
        doublyll.pop()
    assert str(error.value) == "No head to pop"
    with pytest.raises(ValueError) as error:
        doublyll = DLL()
        doublyll.pop()
    assert str(error.value) == "No head to pop"
