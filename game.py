import networkx as nx
import random
from functions import *


G = nx.DiGraph()
G.add_nodes_from(range(14))
edges = [[0,1],[0,2],[0,3],[1,4],[2,4],[3,5],[2,6],[4,7],[5,7],[5,8],[6,8],[6,9],[7,10],[7,11],[8,11],[8,12],[9,13]]
base_costs = [5,6,7,8,11]
G.add_edges_from(edges)

stats = []
for e in edges:
    temp = [e, random.choice(base_costs)*(e[0]+1)]
    temp.append(rate_function(temp[1], e[0]+1))
    stats.append(temp)
time = 0

for x in stats:
    print(x)

