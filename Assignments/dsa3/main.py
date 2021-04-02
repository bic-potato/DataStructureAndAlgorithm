import collections

def html_tag_check(filepath):
    f = open(filepath)

    stack = collections.deque()
