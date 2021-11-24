import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

data = pd.read_csv('csv/follow_relationship.csv', nrows=500)
df = pd.DataFrame({'from': data['user_id'], 'to': data['follower_id']})

# Build your graph. Note that we use the DiGraph function to create the graph!
G = nx.from_pandas_edgelist(df, 'from', 'to', create_using=nx.DiGraph())

# Make the graph
nx.draw(G, with_labels=True, node_size=1500, alpha=0.3, arrows=True)
plt.title("Directed")
plt.savefig("Network_500.png")
