import networkx as nx

g = nx.DiGraph()

# adding the root node
g.add_node('A')

# instead of adding the nodes and then the edges, we can add nodes implicitly
# adding the children of A
g.add_edge('A','B')
g.add_edge('A','C')

# adding the children of B
g.add_edge('B','D')
g.add_edge('B','E')
g.add_edge('B','F')

# adding the children of C
g.add_edge('C','G')

# adding the children of D
g.add_edge('D','H')
g.add_edge('D','I')

# adding the children of F
g.add_edge('F','J')

# adding the children of G
g.add_edge('G','K')
g.add_edge('G','L')
g.add_edge('G','M')

# let networkx test your graph to see if it is actually a tree
print(nx.is_tree(g))

# to get the children of a node use the neighbors function
print('Children of A')
for child in g.neighbors('A'):
    print(child)

# you can also cast it to a list instead of iterating over the children
childrenA = list(g.neighbors('A'))
print(childrenA)

# the neighbors function respects the directionality of the graph
print('Children of B')
for child in g.neighbors('B'):
    print(child)

# you can also cast it to a list instead of iterating over the children
childrenB = list(g.neighbors('B'))
print(childrenB)

# to get the parent(s) of a node use the predecessors function
print('Ancestors of L')
for ancestor in g.predecessors('L'):
    print(ancestor)

# in a normal tree you will only have one parent, but you can have multiple
parentsL = list(g.predecessors('L'))
print(parentsL)

