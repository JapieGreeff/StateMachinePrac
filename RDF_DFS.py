#import random
#from rdflib import Graph, Literal, BNode, Namespace, RDF, URIRef
#from rdflib.namespace import DC, FOAF
from collections import defaultdict
from TreeHelpers import TreeHelpers

helper = TreeHelpers()
g = helper.create_graph()
nodeA = helper.add_node(g,'A')
nodeB = helper.add_node(g,'B')
nodeC = helper.add_node(g,'C')
nodeD = helper.add_node(g,'D')
nodeE = helper.add_node(g,'E')
nodeF = helper.add_node(g,'F')
nodeG = helper.add_node(g,'G')
nodeH = helper.add_node(g,'H')
helper.create_child_relationship(g, nodeA, nodeB)
helper.create_child_relationship(g, nodeB, nodeD)
helper.create_child_relationship(g, nodeB, nodeE)
helper.create_child_relationship(g, nodeA, nodeC)
helper.create_child_relationship(g, nodeC, nodeF)
helper.create_child_relationship(g, nodeC, nodeG)
helper.create_child_relationship(g, nodeF, nodeH)

print(f'nodeA = {nodeA}')
print(f'nodeA children = {helper.get_children(g, nodeA)}')
print(f'nodeB parent = {helper.get_parent(g, nodeB)}')

# testing DFS from A to H with a list being used as a stack
print('testing DFS from A to H with a list being used as a stack')
startNode = nodeA
goalNode = nodeH

openNodes = []
openNodes.append(startNode)
goal = False
while goal is False:
    if openNodes:
        print(openNodes)
        activeNode = openNodes.pop()
        if activeNode == goalNode:
            goal = True
        else:
            children = helper.get_children(g, activeNode)
            for child in children:
                openNodes.append(child)
    else:
        break
if goal:
    backtrackpath = []
    currentNode = goalNode
    backtrackpath.append(currentNode)
    while currentNode is not startNode:
        currentNode = helper.get_parent(g, currentNode)
        backtrackpath.append(currentNode)
    print('backtrack path:')
    for node in backtrackpath:
        print(helper.get_value(g, node))
else:
    print('no path could be found!')
