# https://codefellows.github.io/sea-python-401d6/assignments/binary_heap.html

import pytest

from code_fellows.binary_heap import Heap


@pytest.fixture(scope="function")
def empty_heap():
    return Heap()


@pytest.fixture(scope="function")
def populated_heap():
    test_heap = Heap()
    test_heap.push("one")
    return test_heap


def test_heap_push(empty_heap):
    empty_heap.push("item1")
    assert empty_heap.pop() == "item1"
