from sllist import SingleLinkedList

def test_prepend_list():
    list = SingleLinkedList()
    assert list.head() is None
    list.prepend(1).prepend(2).prepend(3)
    assert list.head() == 3

def test_tail_list():
    list = SingleLinkedList()
    list.prepend(1).prepend(2).prepend(3)
    assert list.tail().head() == 2
    assert list.tail().tail().head() == 1

def test_tail_empty_list():
    list = SingleLinkedList()
    assert list.tail().isEmpty()

def test_size():
    list = SingleLinkedList()
    assert list.size() == 0
    list.prepend(1).prepend(2).prepend(3)
    assert list.size() == 3

def test_contains():
    list = SingleLinkedList()
    list.prepend(5).prepend(9).prepend(1)
    assert list.contains(4) == False
    assert list.contains(5) == True
    assert list.contains(6) == False
    assert list.contains(9) == True
    assert list.contains(77) == False
    assert list.contains(1) == True

def test_join():
    list = SingleLinkedList()
    list.prepend(1).prepend(2).prepend(4)

    list2 = SingleLinkedList()
    list2.prepend(5).prepend(6).prepend(7)

    list.join(list2)

    assert list.head() == 7
    assert list.tail().head() == 6
    assert list.tail().tail().head() == 5
    assert list.tail().tail().tail().head() == 4
    assert list.tail().tail().tail().tail().head() == 2
    assert list.tail().tail().tail().tail().tail().head() == 1

def test_copy():
    list = SingleLinkedList()
    list.prepend(1).prepend(2).prepend(4)

    newList = list.copy()

    list.prepend(5).printToConsole()
    newList.printToConsole()

    assert list.head() == 5
    assert list.tail().head() == 4
    assert list.tail().tail().head() == 2

    assert newList.head() == 4
    assert newList.tail().head() == 2
    assert newList.tail().tail().head() == 1