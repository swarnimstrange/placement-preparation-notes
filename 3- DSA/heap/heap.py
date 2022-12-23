class MaxHeap:
    def __init__(self):
        self.heap = []

    def getParent(self,i):
        return int((i-1)/2)

    def hasParent(self,i):
        return self.getParent(i) < len(self.heap)

    def insert(self,key):
        self.heap.append(key)
        self.heapify(len(self.heap) - 1)

    def heapify(self,i):
        while(self.hasParent(i) and self.heap[i] > self.heap[self.getParent(i)]):
            self.heap[self.getParent(i)], self.heap[i] = self.heap[i], self.heap[self.getParent(i)]
            i = self.getParent(i)

    def printmh(self):
        print(self.heap)

mh = MaxHeap()
mh.insert(5)
mh.insert(6)
mh.insert(7)
mh.insert(10)
mh.insert(3)
mh.insert(12)
mh.insert(8)
mh.printmh()
