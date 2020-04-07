from anytree import Node

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

# the __repr__ function of the node will show us its lineage and name
print(nodeL)
# to get the value of a node use it's name member
print(nodeD.name)
# to get the parent of a node, use the parent member
print(nodeG.parent.name)
# to get a list of the children of a node, use the children member
print(nodeB.children)
for child in nodeB.children:
    print(child.name)
# calling children on a node without children returns an empty list
print(nodeM.children)
# if a node doesn't have a parent it will return None
print(nodeA.parent)
