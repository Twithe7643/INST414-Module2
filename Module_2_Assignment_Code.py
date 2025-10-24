import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt


data = pd.read_csv(r"c:/Users/Twith/OneDrive/414INST Work/listings.csv")


sample = data[['id', 'host_id', 'name', 'neighbourhood', 'price']].head(10)
print(sample)

# Build the host-listing graph
g = nx.Graph()
for _, row in data.iterrows():
    g.add_edge(f"host_{row['host_id']}", f"listing_{row['id']}")

#Prints amount of nodes and edges
print(f"Nodes: {g.number_of_nodes()}, Edges: {g.number_of_edges()}")

#Subsets to only 2 listings with 5-15
hosts_selected = []
for node in g.nodes():
    if node.startswith("host_") and 5 <= g.degree(node) <= 15:
        hosts_selected.append(node)
    if len(hosts_selected) == 4:
        break

# Build a small subgraph with both hosts and their listings
subset_nodes = set()
for host in hosts_selected:
    subset_nodes.add(host)
    subset_nodes.update(g.neighbors(host))

subgraph = g.subgraph(subset_nodes)

# Degree centrality
degree_centrality = nx.degree_centrality(g)
important_nodes = sorted(degree_centrality, key=degree_centrality.get, reverse=True)[:3]
print("Most connected hosts:", important_nodes)

#
node_colors = []
for node in subgraph.nodes():
    if node in hosts_selected:
        node_colors.append("red")   # hosts 
    else:
        node_colors.append("lightblue")  # listings

# Draw network with labels
plt.figure(figsize=(12, 10))
pos = nx.spring_layout(subgraph, seed=40, k=0.2, scale=1)  
nx.draw_networkx_nodes(subgraph, pos, node_color=node_colors, node_size=300)
nx.draw_networkx_edges(subgraph, pos, edge_color="gray")
nx.draw_networkx_labels(subgraph, pos, font_size=5)


plt.title("Listings by Host Network", fontsize=15)
plt.show()