import heapq

class PriorityQueue:
    def __init__(self):
        self.items = []

    def enqueue(self, item, priority):
        # lower numerical value, higher priority
        heapq.heappush(self.items, (priority, item))
    
    def dequeue(self):
        if not self.isEmpty():
            priority, item = heapq.heappop(self.items)
            return item
        else:
            return None
    
    def isEmpty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)#
    

p_queue = PriorityQueue()

p_queue.enqueue(4, 8)
p_queue.enqueue(2, 3)
p_queue.enqueue(1, 2)
p_queue.enqueue(3, 7)

print(p_queue.dequeue())