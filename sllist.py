# defines a node in a singly linked list
class _Node:
    # constructs a node with an element and a next node 
    def __init__(self, element, nextNode):
        self.__element = element
        self.__next = nextNode

    # returns the element at the node
    def get(self):
        return self.__element

    # returns the element at the node
    def update(self, newElement):
        self.__element = newElement
    
    # returns the next node
    def next(self):
        return self.__next

# defines a singly linked list
class SingleLinkedList:
    # constructs an empty singly linked list or if provided a _Node a singly linked list starting with the provided _Node
    def __init__(self, first = None):
        self.__head = first

    # returns the first element in the singly linked list or None if empty
    def head(self):
        if self.isEmpty():
            return None
        else:
            return self.__head.get()

    # updates the first element in the singly linked list or not if empty
    def update(self, newElement):
        if self.isEmpty():
            return None
        else:
            return self.__head.update(newElement)
    
    # returns a singly linked list containing all but the first element
    def tail(self):
        if self.isEmpty():
            return SingleLinkedList()
        else:
            return SingleLinkedList(self.__head.next())

    # adds an element at the front of the singly linked list
    def prepend(self, element):
        self.__head = _Node(element, self.__head)
        return self

    # returns True if the singly linked list does not contain any elements
    def isEmpty(self):
        if self.__head is None:
            return True
        else:
            return False
    
    # returns the number of elements in the list
    def size(self):
        def count(n, node):
            if node is None:
                return n
            else:
                return count(n+1, node.next())

        return count(0, self.__head)

    # places new list in front of current list
    def join(self, newList):
        def joinLoop(listA, listB):
            if not listB.isEmpty():
                joinLoop(listA.prepend(listB.head()), listB.tail())

        joinLoop(self, newList.reverse())

    # prints all elements to console
    def printToConsole(self):
        def printLoop(list):
            if not list.isEmpty():
                print(list.head())
                printLoop(list.tail())

        printLoop(self.reverse())

    # checks if a certain element is in the SingleLinkedList
    def contains(self, element):
        def containsLoop(element, list):
            if list.head() == element:
                return True
            elif list.isEmpty():
                return False
            else:
                return containsLoop(element, list.tail())

        return containsLoop(element, self)

    def reverse(self):
        newList = SingleLinkedList()
        def reverseLoop(startList, list):
            if not list.isEmpty():
                reverseLoop(startList.prepend(list.head()), list.tail())
        
        reverseLoop(newList, self)
        self = newList
        return self

    def copy(self):
        newList = SingleLinkedList()
        def copyLoop(startList, list):
            if not list.isEmpty():
                copyLoop(startList.prepend(list.head()), list.tail())
        
        copyLoop(newList, self)
        return newList.reverse()


def Average(list):
    def averageLoop(val, n, list):
        if list.isEmpty():
            return val / n
        else:
            n += 1
            val += list.head()
            return averageLoop(val, n, list.tail())
    return averageLoop(0, 0, list)
