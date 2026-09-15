class Graph:

    def __init__(self, directed=False):
        self.directed = directed
        self.adjList = {} # can I use a dict? dict()

    def __repr__(self):
        # return f"Directed: {self.directed}"
        graph_str = ""
        for node, neighbors in self.adjList.items():
            graph_str += f"{node} -> {neighbors}\n"
        return graph_str
        pass

    def add_node(self, node):
        if node not in self.adjList:
            self.adjList[node] = []  # set()
        else:
            raise ValueError("Node exist already")
        pass

    def remove_node(self, node):
        if node not in self.adjList:
            raise ValueError("Node does not exist")
        else:
            for neighbors in self.adjList.values():
                neighbors.discard(node)
            del self.adjList[node]
            # self.adjList[node].remove(node)
        pass

    def add_edge(self, from_node, to_node, weight=None):
        if from_node not in self.adjList:
            self.add_node(from_node)
        if to_node not in self.adjList:
            self.add_node(to_node)

        if weight is None:
            self.adjList[from_node].add(to_node)
            if not self.directed:
                self.adjList[to_node].add(from_node)
        else:
            self.adjList[from_node].add((to_node, weight))
            if not self.directed:
                self.adjList[to_node].add((from_node, weight))

        pass

    def remove_edge(self, from_node, to_node):
        if from_node in self.adjList:
            if to_node in self.adjList[from_node]:
                self.adjList[from_node].remove(to_node)
            else:
                raise ValueError("Edge does not exist")
            if not self.directed:
                if from_node in self.adjList[to_node]:
                    self.adjList[to_node].remove(from_node)
        else:
            raise ValueError("Edge does not exist")
        pass

    def get_neighbors(self, node):
        return self.adjList.get(node,set())
        pass

    def has_node(self, node):
        return node in self.adjList
        pass

    def has_edge(self, from_node, to_node):
        if from_node in self.adjList:
            return to_node in self.adjList[from_node]
        return False
        pass

    def get_nodes(self):
        return list(self.adjList.keys())
        pass

    def get_edges(self):
        edges = []
        for from_node, neighbors in self.adjList.items():
            for to_node in neighbors:
                edges.append((from_node, to_node))
        pass

    def bfs(self, start, end):
        visited = set()
        queue = [start]
        order = []

        while queue:
            node = queue.pop(0)
            if node not in visited:
                visited.add(node)
                order.append(node)
                neighbors = self.get_neighbors(node)
                for neighbor in neighbors:
                    if isinstance(neighbor, tuple):
                        neighbor = neighbor[0]
                    if neighbor not in visited:
                        queue.append(neighbor)
        return order
        pass

    def dfs(self, start):
        visited = set()
        stack = [start]
        order = []

        while stack:
            node = stack.pop(0)
            if node not in visited:
                visited.add(node)
                order.append(node)
                neighbors = self.get_neighbors(node)
                for neighbor in sorted(neighbors, reverse=True):
                    if isinstance(neighbor, tuple):
                        neighbor = neighbor[0]
                    if neighbor not in visited:
                        stack.append(neighbor)
        return order

        pass