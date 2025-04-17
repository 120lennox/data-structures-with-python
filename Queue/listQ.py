class Queue:
    def __init__(self):

        # initialising a queue with an empty list
        self.items = []
    
    # check if the queue is empty
    def isEmpty(self):
       return len(self.items) == 0

    # adding an element to the queue
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        if not self.isEmpty():
         self.items.pop(0)

        else:
           return None
    
    def peek(self):
       if not self.isEmpty():
          return self.items[0]
       else:
          return None
    
    def size(self):
       return (len(self.items))
       

list_queue = Queue()

list_queue.enqueue(1)
list_queue.enqueue(2)
list_queue.enqueue(3)
list_queue.enqueue(4)

list_queue.dequeue()
print(list_queue.peek())
