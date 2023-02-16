# https://codefellows.github.io/sea-python-401d6/assignments/deque.html

import pytest

from code_fellows.deque import Deque


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
    # should the deque pop all the way to the head?
    # assert populated_deq.pop() == "head_next"
    # assert populated_deq.size() == 1
    # assert populated_deq.pop() == "head"
    # assert populated_deq.size() == 0


#     assert test_deq.peekleft() == None
#     assert test_deq.peekleft() == None
#     with pytest.raises(ValueError) as error:
#         test_deq.pop()
#     assert str(error.value) == "No tail to pop"
#     with pytest.raises(ValueError) as error:
#         test_deq.popleft()
#     assert str(error.value) == "No head to pop"
#     test_deq.append("new")
#     assert test_deq.head.value == "new"
#     assert test_deq.tail.value == "new"
#     assert test_deq.pop() == "new"
#     assert test_deq.size() == 0
#     test_deq.appendleft("newLeft")
#     assert test_deq.head.value == "newLeft"
#     assert test_deq.tail.value == "newLeft"
#     assert test_deq.popleft() == "newLeft"
#     assert test_deq.size() == 0
