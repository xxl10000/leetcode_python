#
# @lc app=leetcode.cn id=146 lang=python3
#
# [146] LRU 缓存
#

# @lc code=start
# 法1： 自己造轮子，建立Node, doubleList来对应LRU
class Node:
    def __init__(self,key = 0, val = 0, next = None, prev = None) -> None:
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next
        
        
class doubleList:
    def __init__(self) -> None:
        self.head = Node()
        self.tail = Node()
        self.head.next, self.tail.prev = self.tail, self.head
    def update(self, node, v):
        node.val = v
    def delete(self, node):
        #position = self.tail
        node.prev.next, node.next.prev = node.next, node.prev
    def deleteLast(self):
        self.delete(self.tail.prev)

    def insertFront(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        
class LRUCache:

    def __init__(self, capacity: int):
        self.L = doubleList()
        self.d = dict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.d:
            node = self.d[key]
            #self.L.update(node, value)
            self.L.delete(node)
            self.L.insertFront(node)
            
            return self.d[key].val
        else:
            return -1            

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            node = self.d[key]
            self.L.update(node, value)
            self.L.delete(node)
            self.L.insertFront(node)
        else:
            length = len(self.d)
            if length < self.capacity:
                node = Node(key, value)
                self.d[key] = node
                self.L.insertFront(node)
            else:
                lastNode = self.L.tail.prev
                
                # p = self.L.head.next
                # while p != self.L.tail:
                #     print(p.val)
                #     p = p.next
                
                self.d.pop(lastNode.key)
                self.L.deleteLast()
                
                node = Node(key, value)
                self.d[key] = node
                self.L.insertFront(node)
        # for k, v in self.d.items():
        #     print(k, v.val)              
            
lru = LRUCache(2)
lru.put(1,0)
lru.put(2,2)
lru.get(1)
lru.put(3,3)
lru.get(2)
lru.put(4,4)
lru.get(1)
lru.get(3)
lru.get(4)

# 法2： 用OrderedDict，调用库太简单了
from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.d = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.d:
            self.d.move_to_end(key)
            return self.d[key]
        else:
            return -1
    

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            self.d.move_to_end(key)
            #self.d[key] = value
        else:
            Length = len(self.d)
            if Length == self.capacity:
                self.d.popitem(last= False)
        self.d[key] = value
            



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

