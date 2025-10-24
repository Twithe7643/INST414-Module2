import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt


data = pd.read_csv(r"c:/Users/Twith/OneDrive/414INST Work/listings.csv")


print(data.columns)

g = nx.Graph()
for _, row in data.iterrows():
    g.add_edge(f"host_{row['host_id']}", f"listing_{row['id']}")

print(f"Nodes: {g.number_of_nodes()}, Edges: {g.number_of_edges()}")

# Sample a smaller subset for visualization (first 50 nodes)
sample_nodes = list(g.nodes())[:50]
subgraph = g.subgraph(sample_nodes)


degree_centrality = nx.degree_centrality(g)
important_nodes = sorted(degree_centrality, key=degree_centrality.get, reverse=True)[:3]
print("Top 3 most connected nodes:", important_nodes)


nx.draw(subgraph, with_labels=True, node_size=200, font_size=8)
plt.show()