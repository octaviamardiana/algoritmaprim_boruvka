class Graph:
    def __init__(self, vertices):  # Menggunakan __init__ yang benar
        self.V = vertices
        self.graph = []
    
    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def boruvka(self):
        parent = [-1] * self.V
        cheapest = [None] * self.V
        num_trees = self.V
        mst_weight = 0
        mst_edges = []

        while num_trees > 1:
            for i in range(len(self.graph)):
                u, v, w = self.graph[i]
                set_u = self.find(parent, u)
                set_v = self.find(parent, v)

                if set_u != set_v:
                    if cheapest[set_u] is None or cheapest[set_u][2] > w:
                        cheapest[set_u] = [u, v, w]
                    if cheapest[set_v] is None or cheapest[set_v][2] > w:
                        cheapest[set_v] = [u, v, w]

            for node in range(self.V):
                if cheapest[node] is not None:
                    u, v, w = cheapest[node]
                    set_u = self.find(parent, u)
                    set_v = self.find(parent, v)

                    if set_u != set_v:
                        mst_edges.append((u, v, w))
                        mst_weight += w
                        parent[set_u] = set_v
                        num_trees -= 1

            cheapest = [None] * self.V

        return mst_edges, mst_weight
    
    def find(self, parent, i):
        if parent[i] == -1:
            return i
        else:
            return self.find(parent, parent[i])

# Contoh penggunaan
g = Graph(5)
g.add_edge(0, 1, 2)
g.add_edge(0, 3, 6)
g.add_edge(1, 2, 3)
g.add_edge(1, 3, 8)
g.add_edge(1, 4, 5)
g.add_edge(2, 4, 7)
g.add_edge(3, 4, 9)

mst_edges, mst_weight = g.boruvka()
print("MST menggunakan Borůvka:", mst_edges)
print("Total berat MST:", mst_weight)

import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []
    
    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def boruvka(self):
        parent = [-1] * self.V
        cheapest = [None] * self.V
        num_trees = self.V
        mst_weight = 0
        mst_edges = []

        while num_trees > 1:
            for i in range(len(self.graph)):
                u, v, w = self.graph[i]
                set_u = self.find(parent, u)
                set_v = self.find(parent, v)

                if set_u != set_v:
                    if cheapest[set_u] is None or cheapest[set_u][2] > w:
                        cheapest[set_u] = [u, v, w]
                    if cheapest[set_v] is None or cheapest[set_v][2] > w:
                        cheapest[set_v] = [u, v, w]

            for node in range(self.V):
                if cheapest[node] is not None:
                    u, v, w = cheapest[node]
                    set_u = self.find(parent, u)
                    set_v = self.find(parent, v)

                    if set_u != set_v:
                        mst_edges.append((u, v, w))
                        mst_weight += w
                        parent[set_u] = set_v
                        num_trees -= 1

            cheapest = [None] * self.V

        return mst_edges, mst_weight
    
    def find(self, parent, i):
        if parent[i] == -1:
            return i
        else:
            return self.find(parent, parent[i])

# Fungsi untuk menggambar graf
def draw_graph(edges, mst_edges=None):
    G = nx.Graph()

    # Tambahkan semua edge ke graf
    for u, v, w in edges:
        G.add_edge(u, v, weight=w)

    pos = nx.spring_layout(G)  # Posisi node secara otomatis

    # Gambarkan semua edge
    edge_labels = {(u, v): f"{w}" for u, v, w in edges}
    nx.draw(G, pos, with_labels=True, node_color="lightblue", font_weight="bold")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    # Jika MST diberikan, beri highlight
    if mst_edges:
        mst_edges_set = [(u, v) for u, v, _ in mst_edges]
        nx.draw_networkx_edges(G, pos, edgelist=mst_edges_set, edge_color="red", width=2)

    plt.show()

# Contoh penggunaan
g = Graph(5)
g.add_edge(0, 1, 2)
g.add_edge(0, 3, 6)
g.add_edge(1, 2, 3)
g.add_edge(1, 3, 8)
g.add_edge(1, 4, 5)
g.add_edge(2, 4, 7)
g.add_edge(3, 4, 9)

# Temukan MST menggunakan Borůvka
mst_edges, mst_weight = g.boruvka()

print("MST menggunakan Borůvka:", mst_edges)
print("Total berat MST:", mst_weight)

# Gambarkan graf dan MST
draw_graph(g.graph, mst_edges)

