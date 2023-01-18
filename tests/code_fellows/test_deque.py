# https://codefellows.github.io/sea-python-401d6/assignments/deque.html

import pytest

from code_fellows.deque import Deque


def test_deque():
    test_deq = Deque()
    test_deq.appendleft("3")
    assert test_deq.size() == 1
    assert test_deq.peekleft() == "3"
    test_deq.append("2")
    assert test_deq.size() == 2
    assert test_deq.peek() == "2"
    assert test_deq.peekleft() == "3"
    assert test_deq.popleft() == "3"
    assert test_deq.pop() == "2"
    assert test_deq.size() == 0
    assert test_deq.peekleft() == None
    assert test_deq.peekleft() == None
    with pytest.raises(ValueError) as error:
        test_deq.pop()
    assert str(error.value) == "No tail to pop"
    with pytest.raises(ValueError) as error:
        test_deq.popleft()
    assert str(error.value) == "No head to pop"
    assert test_deq.is_empty == True
    test_deq.append("new")
    assert test_deq.is_empty == False
    assert test_deq.head.value == "new"
    assert test_deq.tail.value == "new"
    assert test_deq.pop() == "new"
    assert test_deq.size() == 0
    test_deq.appendleft("newLeft")
    assert test_deq.is_empty == False
    assert test_deq.head.value == "newLeft"
    assert test_deq.tail.value == "newLeft"
    assert test_deq.popleft() == "newLeft"
    assert test_deq.size() == 0
