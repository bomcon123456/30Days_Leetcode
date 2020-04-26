## ORDEREDDICT

from collections import OrderedDict
class LRUCache(OrderedDict):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self:
            return - 1
        
        self.move_to_end(key)
        return self[key]

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self:
            self.move_to_end(key)
        self[key] = value
        if len(self) > self.capacity:
            self.popitem(last = False)
## DOUBLED LINKED LIST
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.table = {}
        self.head, self.tail = Node(-1, -1), Node(-1, -1)
        self.head.next, self.tail.prev = self.tail, self.head

    def get(self, key: int) -> int:
        if key in self.table:
            node = self.table[key]
            self.delete(node)
            self.add_to_front(node.key, node.value)
            return node.value
        return -1
            
    def put(self, key: int, value: int) -> None:
        if key in self.table:
            node = self.table[key]
            self.delete(node)
        elif len(self.table) >= self.cap:
            self.delete(self.tail.prev)
        self.add_to_front(key, value)
        
    def add_to_front(self, key, value):
        node = Node(key, value)
        self.table[key] = node
        node.next, node.prev = self.head.next, self.head
        self.head.next.prev, self.head.next = node, node
    
    def delete(self, node):
        node.prev.next, node.next.prev = node.next, node.prev
        self.table.pop(node.key)
