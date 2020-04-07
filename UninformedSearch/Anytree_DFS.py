#import random
#from rdflib import Graph, Literal, BNode, Namespace, RDF, URIRef
#from rdflib.namespace import DC, FOAF
from collections import defaultdict
#from TreeHelpers import TreeHelpers
from anytree import Node, RenderTree

nodeA = Node('A')

nodeB = Node('B', parent=nodeA)
nodeC = Node('C', parent=nodeA)
nodeD = Node('D', parent=nodeB)
nodeE = Node('E', parent=nodeB)
nodeF = Node('F', parent=nodeB)
nodeG = Node('G', parent=nodeC)
nodeH = Node('H', parent=nodeD)
nodeI = Node('I', parent=nodeD)
nodeJ = Node('J', parent=nodeF)
nodeK = Node('K', parent=nodeG)
nodeL = Node('L', parent=nodeG)
nodeM = Node('M', parent=nodeG)
nodeN = Node('N') # a disconnected node - if you search for this one, no path can be found!

print(f'nodeA = {nodeA}')
print(f'nodeA children = {nodeA.children}')
print(f'nodeB parent = {nodeB.parent}')

# testing DFS from A to I with a list being used as a stack
print('testing DFS from A to I with a list being used as a stack')
startNode = nodeA
goalNode = nodeI

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
            children = activeNode.children
            for child in children:
                openNodes.append(child)
    else:
        break
if goal:
    backtrackpath = []
    currentNode = goalNode
    backtrackpath.append(currentNode)
    while currentNode is not startNode:
        currentNode = currentNode.parent
        backtrackpath.append(currentNode)
    print('backtrack path:')
    for node in reversed(backtrackpath):
        print(node)
else:
    print('no path could be found!')
