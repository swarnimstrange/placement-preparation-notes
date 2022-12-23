queue = []

def enqueue(data):
    queue.append(data)

def dequeue():
    queue.pop(0)

def printQ():
    print(queue)

enqueue(3)
enqueue(4)
enqueue(5)
dequeue()
dequeue()
enqueue(10)
printQ()