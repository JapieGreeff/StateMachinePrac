from collections import defaultdict
from TreeHelpers import TreeHelpers
from queue import Queue

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
nodeI = helper.add_node(g,'I')
nodeJ = helper.add_node(g,'J')
nodeK = helper.add_node(g,'K')
nodeL = helper.add_node(g,'L')
nodeM = helper.add_node(g,'M')


helper.create_child_relationship(g, nodeA, nodeB)
helper.create_child_relationship(g, nodeA, nodeC)
helper.create_child_relationship(g, nodeB, nodeD)
helper.create_child_relationship(g, nodeB, nodeE)
helper.create_child_relationship(g, nodeB, nodeF)
helper.create_child_relationship(g, nodeC, nodeG)
helper.create_child_relationship(g, nodeD, nodeH)
helper.create_child_relationship(g, nodeD, nodeI)
helper.create_child_relationship(g, nodeF, nodeJ)
helper.create_child_relationship(g, nodeG, nodeK)
helper.create_child_relationship(g, nodeG, nodeL)
helper.create_child_relationship(g, nodeG, nodeM)

print(f'nodeA = {nodeA}')
print(f'nodeA children = {helper.get_children(g, nodeA)}')
print(f'nodeB parent = {helper.get_parent(g, nodeB)}')

# testing BFS from A to H with a queue
print('testing BFS from A to I with a queue')
startNode = nodeA
goalNode = nodeI

openNodes = Queue()
openNodes.put(startNode)
goal = False
while goal is False:
    if not openNodes.empty(): 
        activeNode = openNodes.get(block=False)
        if activeNode == goalNode:
            goal = True
        else:
            children = helper.get_children(g, activeNode)
            for child in children:
                openNodes.put(child)
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
    for node in reversed(backtrackpath):
        print(helper.get_value(g, node))
else:
    print('no path could be found!')






