graph = {}

def add_node(data):
    graph[data] = []

def add_edge(v1,v2):
    graph[v1].append(v2)
    graph[v2].append(v1)

def printG():
    print(graph)

add_node("a")
add_node("b")
add_node("c")
add_node("d")
add_edge("a","b")
add_edge("c","a")
printG()