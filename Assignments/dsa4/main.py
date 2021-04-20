from queue import SimpleQueue, Queue
import random

def  radixSort(list):
    """
    Sort your list.
    :param String list:
    :return: deque object
    """
    queue_list = [Queue() for i in range(10)]
    main_queue = Queue()
    max_length = 0
    for token in list:
        max_length = len(token) if max_length < len(token) else max_length
        main_queue.put(token)
    for i in range(max_length):
        while not main_queue.empty():
            j = main_queue.get()
            if len(j) > i:
                queue_list[int(j[max_length - 1 - i])].put(j)
            else:
                queue_list[0].put(j)
        for queues in queue_list:
            while not queues.empty():
                main_queue.put(queues.get())
    return main_queue.queue


def passTheParcel(namelist, seed = 0):
    """
    Hot potato problem.
    :param seed randomseed:
    :param String namelist:
    :param int num:
    :return String Object:
    """
    random.seed(seed)
    queue = Queue()
    for name in namelist:
        queue.put(name)
    while queue.qsize() > 1:
        for _ in range(random.randint(0, queue.qsize())):
            queue.put(queue.get())
        queue.get()
    return queue.get()



if __name__ == '__main__':
    list1 = ['73', "22", "93", "43", "55", "14", "28", "65", "39", "81"]
    # print(radix_sort(list1))
    print(passTheParcel(list1, 0))
