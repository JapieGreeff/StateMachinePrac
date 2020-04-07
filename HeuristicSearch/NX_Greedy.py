# testing greedy algorithm with a priority queue
# using https://pypi.org/project/haversine/ for distances
# using https://anaconda.org/anaconda/networkx for graphs

from haversine import haversine, Unit
from queue import PriorityQueue
import networkx as nx

print('testing Best first (Greedy) search with a priority queue')

g = nx.Graph()

# adding in all of the town nodes
g.add_node('Musina', lat=-22.338056, long=30.041667)
g.add_node('Polokwane', lat=-23.9, long=29.45)
g.add_node('Modimolle', lat=-24.7, long=28.406111)
g.add_node('Mbombela', lat=-25.465833, long=30.985278)
g.add_node('Emalahleni', lat=-25.876583, long=29.200972) # previously Witbank
g.add_node('Pretoria', lat=-25.746389, long=28.188056)
g.add_node('Rustenburg', lat=-25.6544, long=27.2559)
g.add_node('Mahikeng', lat=-25.865556, long=25.643611)
g.add_node('Johannesburg', lat=-26.204361, long=28.041639)
g.add_node('Vryburg', lat=-26.95, long=24.747222)
g.add_node('Klerksdorp', lat=-26.866667, long=26.666667)
g.add_node('Vereeniging', lat=-26.673611, long=27.931944)
g.add_node('Standerton', lat=-26.95, long=29.25)
g.add_node('Kroonstad', lat=-27.645556, long=27.231667)
g.add_node('Bethlehem', lat=-28.233333, long=28.3)
g.add_node('Bloemfontein', lat=-29.1, long=26.216667)
g.add_node('Kimberley', lat=-28.7282, long=24.7499)
g.add_node('Ladysmith', lat=-28.5597, long=29.7808)

# adding in all of the road nodes
g.add_edge('Musina','Polokwane', length=201)
g.add_edge('Polokwane','Modimolle', length=147)
g.add_edge('Polokwane','Mbombela', length=301)
g.add_edge('Modimolle','Rustenburg', length=200)
g.add_edge('Modimolle','Pretoria', length=129)
g.add_edge('Modimolle','Emalahleni', length=227)
g.add_edge('Pretoria','Rustenburg', length=114)
g.add_edge('Pretoria','Emalahleni', length=108)
g.add_edge('Pretoria','Johannesburg', length=59)
g.add_edge('Johannesburg','Vereeniging', length=66)
g.add_edge('Vereeniging','Klerksdorp', length=139)
g.add_edge('Vereeniging','Kroonstad', length=147)
g.add_edge('Vereeniging','Standerton', length=159)
g.add_edge('Standerton','Emalahleni', length=145)
g.add_edge('Standerton','Bethlehem', length=208)
g.add_edge('Emalahleni','Mbombela', length=210)
g.add_edge('Kroonstad','Klerksdorp', length=117)
g.add_edge('Kroonstad','Bethlehem', length=144)
g.add_edge('Kroonstad','Bloemfontein', length=218)
g.add_edge('Bethlehem','Bloemfontein', length=249)
g.add_edge('Klerksdorp','Vryburg', length=214)
g.add_edge('Klerksdorp','Mahikeng', length=170)
g.add_edge('Klerksdorp','Rustenburg', length=171)
g.add_edge('Vryburg','Mahikeng', length=159)
g.add_edge('Mahikeng','Rustenburg', length=196)

# helper function for calculating the haversine distance between two points
def haversineCalc(g, nodeA, nodeB):
    latA = g.nodes[nodeA]['lat']
    longA = g.nodes[nodeA]['long']
    latB = g.nodes[nodeB]['lat']
    longB = g.nodes[nodeB]['long']
    return haversine((latA, longA), (latB, longB))
    

# search using the Best first (greedy) approach. As we are using a cyclic graph we need to have a closed list too
startNode = 'Musina'
goalNode = 'Bethlehem'

openNodes = PriorityQueue()
closedNodes = []
parents = {}
dist = haversineCalc(g, startNode, goalNode)
openNodes.put((dist, startNode))
parents[startNode] = None
goal = False
while goal is False:
    if not openNodes.empty(): 
        value = openNodes.get()
        dist = value[0]
        activeNode = value[1]
        closedNodes.append(activeNode)
        if activeNode == goalNode:
            goal = True
        else:
            children = g.neighbors(activeNode)
            for child in children:
                if child not in closedNodes:
                    dist = haversineCalc(g, child, goalNode)
                    openNodes.put((dist, child))    # append the child node as well as it's haversine distance to the goal
                    parents[child] = activeNode
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
