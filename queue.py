# queue.py - Implementación de Queue usando deque
from collections import deque

class Queue:
    """Queue implementado con collections.deque para O(1) en ambos extremos"""
    def __init__(self):
        self.items = deque()
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        return self.items.popleft() if self.items else None
    
    def front(self):
        return self.items[0] if self.items else None
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)