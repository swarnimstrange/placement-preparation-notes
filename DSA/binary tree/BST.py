class Bst:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def search(self,data):
        if self.key == data:
            print("Found")
        elif self.key < data:
            if self.right:
                self.right.search(data)
            else:
                print("Not Found")
        else:
            if self.left:
                self.left.search(data)
            else:
                print("Not found")

    def insert(self,data):
        if self.key is None:
            self.key = data
            return
        if self.key < data:
            if self.right:
                self.right.insert(data)
            else:
                self.right = Bst(data)
        else:
            if self.left:
                self.left.insert(data)
            else:
                self.left = Bst(data)

    
    def delete(self,data):
        if self.key is None:
            print("Tree is empty!")
        elif self.key < data:
            if self.right:
                self.right = self.right.delete(data)
            else:
                print("Node is not found!")
        elif self.key > data:
            if self.left:
                self.left = self.left.delete(data)
            else:
                print("Node is not Found!")
        else:
            if self.left is None:
                temp = self.right
                self = None
                return temp
            if self.right is None:
                temp = self.left
                self = None
                return temp
            node = self.right
            while node.left:
                node = node.left
            self.key = node.key
            self.right = self.right.delete(node.key)
        return self

    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.key)
        if self.right:
            self.right.inorder()

bst = Bst(50)
bst.insert(30)
bst.insert(20)
bst.insert(40)
bst.insert(70)
bst.insert(60)
bst.delete(50)
bst.inorder()
