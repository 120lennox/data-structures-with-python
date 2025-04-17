import heapq

class PriorityQueue:
    def __init__(self):
        self.items = []

    def enqueue(self, item, priority):
        # lower numerical value, higher priority
        heapq.heappush(self.elements, (priority, item))
    
    def dequeue(self):
        if not self.isEmpty():
            priority, item = heapq.heappop(self.items)
            return item
        else:
            return None
    
    def isEmpty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)