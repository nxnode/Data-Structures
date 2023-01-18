# https://codefellows.github.io/sea-python-401d6/assignments/deque.html

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
    assert test_deq.pop() == ""
