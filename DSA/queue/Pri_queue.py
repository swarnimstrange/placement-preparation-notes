class PriorityQueue():

    def __init__(self):
        self.priQ = []

    def insert(self,data):
        self.priQ.append(data)

    def isEmpty(self):
        if self.priQ == []:
            return True

    def delete(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            maxi = max(self.priQ)
            print(maxi)
            self.priQ.remove(maxi)

    def printPQ(self):
        print(self.priQ)

PQ = PriorityQueue()
PQ.insert(5)
PQ.insert(1)
PQ.insert(3)
PQ.insert(6)
PQ.printPQ()
while PQ.isEmpty() is not True:
    PQ.delete()

    

