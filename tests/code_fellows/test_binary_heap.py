# https://codefellows.github.io/sea-python-401d6/assignments/binary_heap.html

import pytest

from code_fellows.binary_heap import Heap


@pytest.fixture(scope="function")
def heap():
    return Heap()


@pytest.fixture(scope="function")
def populated_heap():
    test_heap = Heap()
    test_heap.push("one")
    return test_heap


def test_heap_push(heap):
    heap.push(1)
    assert heap.root.value == 1
    assert heap.root.child_left == None
    assert heap.root.child_right == None
    heap.push(3)
    assert heap.root.value == 1
    assert heap.root.child_left.value == 3
    assert heap.root.child_right == None
    assert heap.root.child_left.parent.value == 1
    assert heap.root.child_left.child_left == None
    assert heap.root.child_left.child_right == None
    heap.push(2)
    assert heap.root.value == 1
    assert heap.root.child_left.value == 2
    assert heap.root.child_right.value == 3
    assert heap.root.child_left.parent.value == 1
    assert heap.root.child_right.parent.value == 1
    assert heap.root.child_left.child_left == None
    assert heap.root.child_left.child_right == None
    assert heap.root.child_right.child_left == None
    assert heap.root.child_right.child_right == None
