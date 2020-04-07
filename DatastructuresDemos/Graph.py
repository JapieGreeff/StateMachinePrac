import networkx as nx

g = nx.Graph()

# adding nodes to the graph. You can add as many attributes as you want
g.add_node(1, foo='A', xyz='XYZ', count=123)
g.add_node(2, foo='B')
g.add_node(3, foo='C')
g.add_node(4, foo='D')
g.add_node(5, foo='E')
g.add_node(6, foo='F')

# adding edges between nodes. Edge attributes are added the same way as node attributes
g.add_edge(1, 2, bar='a', abc='ABX', count=789)
g.add_edge(1, 5, bar='b')
g.add_edge(2, 3, bar='c')
g.add_edge(2, 5, bar='d')
g.add_edge(3, 4, bar='e')
g.add_edge(4, 5, bar='f')
g.add_edge(4, 6, bar='g')

# accessing nodes from the nodes member returns a dictionary of their data
print(g.nodes[1])

# getting specific data is done as one would do with any dictionary
print(g.nodes[1]['foo'])

# getting data from an edge is done similarly but without specifying that it is a node
print(g[1][2])

# and accessing the data in the dictionary is done in the same way
print(g[1][2]['bar'])

# getting all of the adjacent nodes can be done with the neighbors function (returns an iterator)
for neighbor in g.neighbors(1):
    print(neighbor)
