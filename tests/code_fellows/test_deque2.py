# https://codefellows.github.io/sea-python-401d6/assignments/deque.html

import pytest

from code_fellows.deque2 import Deque


@pytest.fixture(scope="function")
def empty_deq():
    return Deque()


@pytest.fixture(scope="function")
def populated_deq():
    test_deq = Deque()
    test_deq.appendleft("head_next")
    test_deq.appendleft("head")
    test_deq.append("tail_prev")
    test_deq.append("tail")
    return test_deq


def test_deque_appendleft_and_popleft(empty_deq):
    empty_deq.appendleft("head")
    assert empty_deq.size() == 1
    assert empty_deq.peekleft() == "head"
    assert empty_deq.popleft() == "head"
    assert empty_deq.size() == 0
    with pytest.raises(ValueError) as exc_info:
        empty_deq.popleft()
    expected = "No head to pop"
    assert expected in str(exc_info.value)
    assert empty_deq.peekleft() is None


def test_deq_append_and_pop(empty_deq):
    empty_deq.append("tail")
    assert empty_deq.size() == 1
    assert empty_deq.peek() == "tail"
    assert empty_deq.pop() == "tail"
    assert empty_deq.size() == 0
    with pytest.raises(ValueError) as exc_info:
        empty_deq.pop()
    expected = "No tail to pop"
    assert expected in str(exc_info.value)
    assert empty_deq.peek() is None
    assert empty_deq.__len__() == 0


def test_deq_pop_and_size(populated_deq):
    assert populated_deq.size() == 4
    assert populated_deq.pop() == "tail"
    assert populated_deq.size() == 3
    assert populated_deq.pop() == "tail_prev"
    assert populated_deq.size() == 2


def test_deq_append(empty_deq):
    empty_deq.append("head")
    empty_deq.append("torso")
    empty_deq.append("tail")
    assert empty_deq.size() == 3
    assert empty_deq.peekleft() == "head"
    assert empty_deq.peek() == "tail"


def test_deq_appendleft(empty_deq):
    empty_deq.appendleft("tail")
    empty_deq.appendleft("torso")
    empty_deq.appendleft("head")
    assert empty_deq.size() == 3
    assert empty_deq.peekleft() == "head"
    assert empty_deq.peek() == "tail"


def test_deq_pop(populated_deq):
    assert populated_deq.pop() == "tail"
    populated_deq.pop()
    populated_deq.pop()
    assert populated_deq.pop() == "head"
    assert populated_deq.size() == 0
    with pytest.raises(ValueError):
        populated_deq.pop()


def test_deq_popleft(populated_deq):
    assert populated_deq.popleft() == "head"
    populated_deq.popleft()
    populated_deq.popleft()
    assert populated_deq.popleft() == "tail"
    assert populated_deq.size() == 0
    with pytest.raises(ValueError):
        populated_deq.popleft()
