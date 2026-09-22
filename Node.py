from Edge import Edge

class Node:
    def __init__(self, name, edges):
        self.name = name
        self.edges = edges

    def __str__(self):
        return None

    def add_edge(self, target_node, weight):
        pass

    def get_edges(self):
        return self.edges
    
