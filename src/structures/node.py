class Node:
    def __init__(self, data, cur_mn=None):
        self.data = data
        self.next = None
        self.prev = None
        self.cur_mn = cur_mn
