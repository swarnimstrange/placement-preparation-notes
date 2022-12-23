class Graph:
    def __init__(self):
        self.nodes = []
        self.graph = []
        self.node_count = 0

    def add_node(self,data):
        self.nodes.append(data)
        self.node_count +=1
        for i in self.graph:
            i.append(0)
        temp = []
        for i in range(self.node_count):
            temp.append(0)
        self.graph.append(temp)

    def printGraph(self):
        print(self.nodes)
        for i in range(self.node_count):
            for j in range(self.node_count):
                print(self.graph[i][j], end=" ")
            print()

    def add_edge(self,v1,v2):
        from_index = self.nodes.index(v1)
        to_index = self.nodes.index(v2)
        self.graph[from_index][to_index] = 1
        self.graph[to_index][from_index] = 1

g = Graph()
g.add_node("a")
g.add_node("b")
g.add_node("c")
g.add_edge("a","b")
g.add_edge("c","b")
g.printGraph()

        