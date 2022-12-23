class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def printLL(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            while self.head is not None:
                print(self.head.data, "-> ",end="")
                self.head = self.head.next

    def deleteNode(self,elem):
        nextnode = self.head
        prevnode = None
        if self.head.data == elem:
            self.head = self.head.next 
        else:
            while nextnode is not None:
                prevnode = nextnode
                nextnode = nextnode.next
                if nextnode.data == elem:
                    break
            if nextnode.data == elem:
                prevnode.next = nextnode.next
            else:
                print("Element does not exist in Linked List")



    def insertAtPos(self,data,pos):
        newnode = Node(data)
        if pos==0:
            newnode.next = self.head
            self.head = newnode
        else:
            count = 1
            nextnode = self.head
            while nextnode is not None and count<=pos:
                if count == pos:
                    newnode.next = nextnode.next 
                    nextnode.next = newnode
                    break
                nextnode = nextnode.next
                count+=1
            else:
                print("Position not found")

    def insertAfter(self,data,elem):
        newnode = Node(data)
        nextnode = self.head
        while nextnode is not None:
            if nextnode.data == elem:
                newnode.next = nextnode.next
                nextnode.next = newnode
                break
            nextnode = nextnode.next
        else:
            print("element not present")



    def insertEnd(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            nextnode = self.head
            while nextnode.next is not None:
                nextnode = nextnode.next
            newnode = Node(data)
            nextnode.next = newnode

    def insertBeg(self,data):
        if self.head is None:
            self.head = Node(data)
        else:
            newnode = Node(data)
            newnode.next =  self.head
            self.head = newnode

    def reverseLL(self):
        nextnode = self.head
        prev = None
        while nextnode is not None:
            temp = nextnode.next
            nextnode.next = prev
            prev = nextnode
            nextnode = temp
        self.head = prev
        

LL = LinkedList()
LL.insertBeg(1)
LL.insertBeg(3)
LL.insertBeg(5)
LL.reverseLL()
LL.printLL()