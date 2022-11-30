class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.container = [None for _ in range(self.size)]
        self.front = 0
        self.rear = 0
    
    def is_empty(self):
        return self.front == self.rear
    
    def step_forward(self, index):
        index += 1
        if index >= self.size:
            index = 0
        return index
    
    def is_full(self):
        next = self.step_forward(self.rear)
        return next == self.front
    
    def enqueue(self, data):
        if self.is_full():
            raise Exception("The queue is full")
        
        self.container[self.rear] = data
        self.rear = self.step_forward(self.rear)
    
    def dequeue(self):
        if self.is_empty():
            raise Exception("The Queue is empty")
        
        ret = self.container[self.front]
        self.container[self.front] = None
        self.front = self.step_forward(self.front)
        return ret

    def peek(self):
        if self.is_empty():
            raise Exception("The Queue is empty")
        
        return self.container[self.front]

cq = CircularQueue(10)

for i in range(8):
    cq.enqueue(i)

for i in range(5):
    print(cq.dequeue(), end="  ")

for i in range(8,14):
    cq.enqueue(i)
