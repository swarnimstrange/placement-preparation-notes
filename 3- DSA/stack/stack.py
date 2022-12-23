stack = []

def push(elem):
    stack.append(elem)

def pop():
    stack.pop()

def printS():
    print(stack)

push(1)
push(3)
push(6)
push(5)
pop()
printS()