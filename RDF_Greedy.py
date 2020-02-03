# testing greedy algorithm with a priority queue
# using https://pypi.org/project/haversine/ for distances

import random
from rdflib import Graph, Literal, BNode, Namespace, RDF, URIRef, term
from rdflib.namespace import XSD
from rdflib.namespace import DC, FOAF
from collections import defaultdict
from haversine import haversine, Unit
from PriorityQueue import PriorityQueue
print('testing Best first (Greedy) search with a priority queue')

# for this example, we will use an imaginary map. We will use the Best first (greedy) algorithm to give us the shortest path from one part of the map to the other
# Latitude and Longitude for the cities and towns in our minimal map


# a node is a town name, lat, long
def add_town(graph, name, lat, long):
    node = Literal(name) # can also be a BNode
    graph.add( (node, RDF.type, Literal('town')) )
    graph.add( (node, Literal('latitude'), Literal(lat)) )
    graph.add( (node, Literal('longitude'), Literal(long)) )
    return node

# a road is a distance and two nodes
def add_road(graph, length, nodeA, nodeB):
    road = BNode()
    graph.add( (road, RDF.type, Literal('road')) )
    graph.add( (road, RDF.value, Literal(length)) )
    graph.add( (road, Literal('endpoint'), nodeA) )
    graph.add( (road, Literal('endpoint'), nodeB) )

def haversine_distance(graph, nodeA, nodeB):
    # gets the distance as the crow flies between two nodes
    nodeALat = term._castLexicalToPython(graph.value(subject=nodeA, predicate=Literal('latitude')), XSD.float)
    nodeALon = term._castLexicalToPython(graph.value(subject=nodeA, predicate=Literal('longitude')), XSD.float)
    nodeBLat = term._castLexicalToPython(graph.value(subject=nodeB, predicate=Literal('latitude')), XSD.float)
    nodeBLon = term._castLexicalToPython(graph.value(subject=nodeB, predicate=Literal('longitude')), XSD.float)

    return haversine((nodeALat, nodeALon), (nodeBLat, nodeBLon))

def connected_towns(graph, node, goalnode):
    roads = list(graph.subjects(predicate=Literal('endpoint'), object=node))
    # for each road you want the "other" endpoint which is the destination town
    connected = []
    for road in roads:
        endpoints = list(graph.objects(subject=road, predicate=Literal('endpoint')))
        otherNode = None
        for endpoint in endpoints:
            if endpoint is not node:
                otherNode = endpoint
        roadlength = term._castLexicalToPython(graph.value(subject=road, predicate=RDF.value), XSD.integer)
        connected.append((otherNode, haversine_distance(graph, otherNode, goalnode), roadlength))
    return connected

g = Graph()

# adding in all of the town nodes
musina = add_town(g, 'Musina', -22.338056, 30.041667)
polokwane = add_town(g, 'Polokwane', -23.9, 29.45)
modimolle = add_town(g, 'Modimolle', -24.7, 28.406111)
mbombela = add_town(g, 'Mbombela', -25.465833, 30.985278)
emalahleni = add_town(g, 'Emalahleni', -25.876583, 29.200972)
pretoria = add_town(g, 'Pretoria', -25.746389, 28.188056)
rustenburg = add_town(g, 'Rustenburg', -25.6544, 27.2559)
mahikeng = add_town(g, 'Mahikeng', -25.865556, 25.643611)
johannesburg = add_town(g, 'Johannesburg', -26.204361, 28.041639)
vryburg = add_town(g, 'Vryburg', -26.95, 24.747222)
klerksdorp = add_town(g, 'Klerksdorp', -26.866667, 26.666667)
vereeniging = add_town(g, 'Vereeniging', -26.673611, 27.931944)
standerton = add_town(g, 'Standerton', -26.95, 29.25)
kroonstad = add_town(g, 'Kroonstad', -27.645556, 27.231667)
bethlehem = add_town(g, 'Bethlehem', -28.233333, 28.3)
bloemfontein = add_town(g, 'Bloemfontein', -29.1, 26.216667)

# adding in all of the road nodes
add_road(g, 201, musina, polokwane)
add_road(g, 147, polokwane, modimolle)
add_road(g, 301, polokwane, mbombela)
add_road(g, 200, modimolle, rustenburg)
add_road(g, 129, modimolle, pretoria)
add_road(g, 227, modimolle, emalahleni)
add_road(g, 114, pretoria, rustenburg)
add_road(g, 108, pretoria, emalahleni)
add_road(g, 59, pretoria, johannesburg)
add_road(g, 66, johannesburg, vereeniging)
add_road(g, 139, vereeniging, klerksdorp)
add_road(g, 147, vereeniging, kroonstad)
add_road(g, 159, vereeniging, standerton)
add_road(g, 145, standerton, emalahleni)
add_road(g, 208, standerton, bethlehem)
add_road(g, 210, emalahleni, mbombela)
add_road(g, 117, kroonstad, klerksdorp)
add_road(g, 144, kroonstad, bethlehem)
add_road(g, 218, kroonstad, bloemfontein)
add_road(g, 249, bethlehem, bloemfontein)
add_road(g, 214, klerksdorp, vryburg)
add_road(g, 170, klerksdorp, mahikeng)
add_road(g, 171, klerksdorp, rustenburg)
add_road(g, 159, vryburg, mahikeng)
add_road(g, 196, mahikeng, rustenburg)


#print(connected_towns(g, pretoria, bloemfontein))

# search using the Best first (greedy) approach. As we are using a cyclic graph we need to have a closed list too

startNode = musina
goalNode = bethlehem

openNodes = PriorityQueue()
closedNodes = []
parents = {}
openNodes.push(startNode, haversine_distance(g, startNode, goalNode))
parents[startNode] = None
goal = False
n = 0
while goal is False:
    if openNodes.not_empty(): 
        n = n + 1
        print(f'iteration {n}:')
        print(f'open: {openNodes}')
        print(f'closed: {closedNodes}\n')
        activeNode, dist = openNodes.pop()
        closedNodes.append(activeNode)
        if activeNode == goalNode:
            goal = True
        else:
            children = connected_towns(g, activeNode, goalNode)
            for child in children:
                if child[0] not in closedNodes:
                    openNodes.push(child[0], child[1])    # append the child node as well as it's haversine distance to the goal
                    parents[child[0]] = activeNode
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
    for node in backtrackpath:
        print(node)
else:
    print('no path could be found!')