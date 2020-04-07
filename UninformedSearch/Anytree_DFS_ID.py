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

# testing DFS from A to I with a list being used as a stack with iterative deepening
print(' testing DFS from A to I with a list being used as a stack with iterative deepening')
startNode = nodeA
goalNode = nodeI

def iterativeDeepening(start, goal):
    def boundDFS(activeNode, finalNode, depth, limit):
        if activeNode == finalNode:
            return True, activeNode
        children = list(activeNode.children)
        while len(children) > 0 and depth < limit:
            result, foundNode = boundDFS(children.pop(), finalNode, depth + 1, limit)
            if result:
                return True, foundNode
        return False, None

    depthLimit = 0
    goalFound = False
    foundNode = None
    while not goalFound and depthLimit < 5:
        goalFound, foundNode = boundDFS(start, goal, 0, depthLimit)
        depthLimit = depthLimit + 1
    if foundNode:
        backtrackpath = []
        currentNode = foundNode
        backtrackpath.append(currentNode)
        while currentNode is not start:
            currentNode = currentNode.parent
            backtrackpath.append(currentNode)
        print('backtrack path:')
        for node in reversed(backtrackpath):
            print(node)
    else:
        print('no path could be found!')

iterativeDeepening(startNode,goalNode)