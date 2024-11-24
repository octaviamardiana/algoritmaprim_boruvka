# Definisi adjacency matrix graf
graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]

# Fungsi algoritma Prim
def prim(graph):
    num_vertices = len(graph)
    selected_nodes = [False] * num_vertices
    edges = []
    total_weight = 0

    selected_nodes[0] = True  # Start from the first vertex

    while len(edges) < num_vertices - 1:
        minimum = float('inf')
        x = 0
        y = 0
        
        for i in range(num_vertices):
            if selected_nodes[i]:
                for j in range(num_vertices):
                    if not selected_nodes[j] and graph[i][j]:  # Check for edge
                        if minimum > graph[i][j]:
                            minimum = graph[i][j]
                            x, y = i, j
        
        edges.append((x, y, graph[x][y]))
        total_weight += graph[x][y]
        selected_nodes[y] = True

    return edges, total_weight

# Jalankan algoritma Prim
mst_edges, mst_weight = prim(graph)

print("MST menggunakan Prim:", mst_edges)
print("Total berat MST:", mst_weight)

# Visualisasi graf
import networkx as nx
import matplotlib.pyplot as plt

def visualize_graph(graph, mst_edges):
    G = nx.Graph()

    # Tambahkan semua simpul dan sisi ke graf awal
    num_vertices = len(graph)
    for i in range(num_vertices):
        for j in range(i+1, num_vertices):  # Hindari duplikasi sisi
            if graph[i][j] != 0:
                G.add_edge(i, j, weight=graph[i][j])

    # Tambahkan sisi MST dengan warna khusus
    mst_edges_set = {(u, v) for u, v, _ in mst_edges}
    edge_colors = []
    for u, v in G.edges():
        if (u, v) in mst_edges_set or (v, u) in mst_edges_set:
            edge_colors.append('red')  # MST edge in red
        else:
            edge_colors.append('black')  # Non-MST edge in black

    # Posisi simpul untuk tata letak visual
    pos = nx.spring_layout(G)

    # Gambarkan graf
    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color=edge_colors, node_size=500, font_size=10)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    plt.title("Visualisasi Graf dan MST")
    plt.show()

# Visualisasi hasil
visualize_graph(graph, mst_edges)
