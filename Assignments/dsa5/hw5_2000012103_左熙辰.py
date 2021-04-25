"""
Data Structure and Algorithm: Homework 5 Template.
Version: 3.6
Date: 2019-04-07
Note:
    Your homework name must be 'hw5_[student id]_[name].py'.
    e.x: hw5_1700013200_xxx.py
"""


class Node:
    def __init__(self, init_data=None, next=None, last=None):
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


class HeaderNode(Node):
    def __init__(self, init_data=None, next=None, last=None):
        super().__init__(init_data, next, last)
        self.next = None

    def get_data(self):
        pass

    def set_data(self, new_data):
        pass

    def get_last(self):
        pass

    def get_next(self):
        pass

    def set_last(self, new_last):
        pass


class UnorderedList:
    def __init__(self):
        self.prehead = HeaderNode()
        self.head = None
        self.prehead.set_next(self.head)
        self.tail = None

    def add(self, item):
        node = Node(item)
        if not self.is_empty:
            node.next = self.head
            self.head = node
        else:
            node.next = self.head
            self.head = node
            self.tail = node
        self.prehead.next = self.head
        return 0

    def size(self):
        cur = self.prehead
        count = 0
        while cur.next is not None:
            count += 1
            cur = cur.next
        return count

    def search(self, item):
        cur = self.head
        while cur.next is not None:
            if cur.data == item:
                return True
            cur = cur.next
        return False

    def remove(self, item):
        cur = self.prehead
        while cur.next.next is not None:
            if cur.next.data == item:
                cur.next == cur.next.next
                return 0
            cur = cur.next
            self.prehead.next = self.head
        else:
            if cur.next.data == item:
                cur.next = None
                self.tail = cur
            else:
                raise ValueError("item not in list")

    def append(self, item):
        node = Node(item)
        if self.is_empty:
            self.tail = node
            self.head = node
        else:
            self.tail.next = node
            self.tail = node
        self.prehead.next = self.head
        return 0

    def index(self, item):
        index = 0
        cur = self.prehead
        while cur.next is not None:
            if cur.data != item:
                index += 1
                cur = cur.next
            else:
                return index
        raise IndexError("List Index Out of Range")

    @property
    def is_empty(self):
        return self.head is None

    def __str__(self):
        cur = self.prehead
        list1 = []
        while cur.next is not None:
            cur = cur.next
            list1.append(cur.data)
        return str(list1)

    def __getitem__(self, ind):
        index = 0
        cur = self.head
        if ind < 0:
            ind += self.size()
        while cur.next is not None:
            if index == ind:
                return cur
            else:
                index += 1
                cur = cur.next
        else:
            if index == ind:
                return cur
        raise IndexError

    def pop(self, pos=-1):
        popout = self[pos].data
        self.remove(self[pos].data)
        return popout

    def insert(self, ind, item):
        node = Node(item)
        pre_node = self[ind]
        post_node = pre_node.next
        node.next = post_node
        pre_node.next = node
        return None


class OrderedList(UnorderedList):

    def add(self, item):
        node = Node(item)
        current = self.prehead
        stop = False
        if self.is_empty:
            self.head = node
            self.prehead.next = self.head
        else:
            while current.next is not None and not stop:
                if current.next.data > item:
                    stop = True
                else:
                    current = current.next
            if current.next is None:
                current.next = node
                self.tail = node
            else:
                node.next = current.next
                current.next = node
        self.prehead.next = self.head
        return None

    def search(self, item):
        low = 0
        high = self.size() - 1
        while low <= high:
            mid = (low + high) // 2
            if self[mid].data == item:
                return mid
            elif self[mid].data > item:
                high = mid - 1
            else:
                low = mid + 1
        raise ValueError


class Stack:
    def __init__(self):
        self.__data = UnorderedList()

    def push(self, item):
        self.__data.append(item)
        return None

    def pop(self):
        data = self.__data.pop()
        return data

    def peek(self):
        return self.__data[-1]

    def is_empty(self):
        return self.__data.is_empty

    @property
    def size(self):
        return self.__data.size()

    def __str__(self):
        return str(self.__data)


class Queue:
    def __init__(self):
        self.__data = UnorderedList()
        return

    def enqueue(self, item):
        self.__data.add(item)
        return None

    def dequeue(self):
        data = self.__data.pop()
        return data

    @property
    def is_empty(self):
        return self.__data.is_empty

    @property
    def size(self):
        return self.__data.size()

    def __str__(self):
        return str(self.__data)


def test():
    """
    Only a simple test.
    Make sure your homework can at least successfully run this test.
    :return:
    """
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
    print(lst)
    assert str(lst) == str(sorted(test_lst))  # modified: test_lst.sort() -> sorted(test_lst)
    print(stk.size)
    print(stk)
    assert stk.size == len(test_lst)
    print(queue.size)
    assert queue.size == len(test_lst)
    print(unlst[-1].data)
    assert stk.pop() == 4
    assert queue.dequeue() == 1
    assert unlst.tail.get_data() == 4


if __name__ == '__main__':
    test()
