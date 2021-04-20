'''
Data Structure and Algorithm: Homework 5 Template.
Version: 3.6
Date: 2019-04-07
Note:
    Your homework name must be 'hw5_[student id]_[name].py'.
    e.x: hw5_1700013200_xxx.py
'''


class Node:
    def __init__(self, init_data, next=None, last=None):
        self.data = init_data
        self.next = next
        self.last = last

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def get_last(self):
        return self.last

    def set_data(self, new_data):
        self.data = new_data
        return 0

    def set_next(self, new_next):
        self.next = new_next
        return 0

    def set_last(self, new_last):
        self.last = new_last
        return 0


class UnorderedList:
    def __init__(self):
        self.data = Node(None)
        self.head = self.data.next
        self.tail = self.data.next

    def add(self, item):
        self.tail.next = Node(item)
        self.tail.next.last = self.tail.
        self.tail = self.tail.next
        return 0

    def size(self):
        temp = self.data
        count = 0
        while temp.next() != None:
            count += 1
            temp = temp.next()
        return count

    def serach(self, item):
        # TODO:
        return

    def remove(self, item):
        # TODO:
        return

    def append(self, item):
        # TODO:
        return

    def index(self, item):
        # TODO:
        return

    def __str__(self):
        # TODO:
        return

    def __getitem__(self, ind):
        # TODO:
        return

    def pop(self, pos=-1):
        # TODO:
        return

    def insert(self, ind, item):
        # TODO:
        return


class OrderedList(UnorderedList):
    def __init__(self):
        # TODO:
        return

    def add(self):
        # TODO:
        return

    def serach(self, item):
        # TODO:
        return


class Stack:
    def __init__(self):
        # TODO:
        return

    def push(self, item):
        # TODO:
        return

    def pop(self):
        # TODO:
        return

    def peek(self):
        # TODO:
        return

    def is_empty(self):
        # TODO:
        return

    def size(self):
        # TODO:
        return


class Queue:
    def __init__(self):
        # TODO:
        return

    def enqueue(self, item):
        # TODO:
        return

    def dequeue(self):
        # TODO:
        return

    def is_empty(self):
        # TODO:
        return

    def size(self):
        # TODO:
        return


def test():
    '''
    Only a simple test.
    Make sure your homework can at least successfully run this test.
    :return:
    '''
    test_lst = [1, 3, 5, 2, 4]
    unlst = UnorderedList()
    lst = OrderedList()
    stk = Stack()
    queue = Queue()
    for x in test_lst:
        unlst.append(x)  # modified: add -> append
        lst.add(x)
        stk.push(x)
        queue.enqueue(x)
    assert str(unlst) == str(test_lst)
    assert str(lst) == str(sorted(test_lst))  # modified: test_lst.sort() -> sorted(test_lst)
    assert stk.size() == len(test_lst)
    assert queue.size() == len(test_lst)
    assert stk.pop() == 4
    assert queue.dequeue() == 1
    assert unlst.tail.get_data() == 4


if __name__ == '__main__':
    test()
