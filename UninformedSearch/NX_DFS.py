from queue import Queue
import networkx as nx

g = nx.Graph()
g.add_node('A')
g.add_node('B')
g.add_node('C')
g.add_node('D')
g.add_node('E')
g.add_node('F')
g.add_node('G')
g.add_node('H')
g.add_node('I')
g.add_node('J')
g.add_node('K')
g.add_node('L')
g.add_node('M')
g.add_node('N')

g.add_edge('A','B')
g.add_edge('A','C')
g.add_edge('B','D')
g.add_edge('B','E')
g.add_edge('B','F')
g.add_edge('C','G')
g.add_edge('D','H')
g.add_edge('D','I')
g.add_edge('F','J')
g.add_edge('G','K')
g.add_edge('G','L')
g.add_edge('G','M')

# testing BFS from A to I with a queue
print('testing BFS from A to I with a queue')
startNode = 'A'
goalNode = 'I'
parents = {}
parents[startNode] = None
openNodes = []
openNodes.append(startNode)
closedNodes = []
goal = False
while goal is False:
    if openNodes: 
        activeNode = openNodes.pop()
        if activeNode == goalNode:
            goal = True
        else:
            children = g.neighbors(activeNode)
            closedNodes.append(activeNode)
            for child in children:
                if child not in closedNodes:
                    parents[child] = activeNode
                    openNodes.append(child)
    else:
        break
if goal:
    backtrackpath = []
    currentNode = goalNode
    backtrackpath.append(currentNode)
    while currentNode is not startNode:
        currentNode = parents[currentNode]
        backtrackpath.append(currentNode)
    print('backtrack path:')
    for node in reversed(backtrackpath):
        print(node)
else:
    print('no path could be found!')






