# testing A* algorithm with a priority queue
# using https://pypi.org/project/haversine/ for distances

import random
from rdflib import Graph, Literal, BNode, Namespace, RDF, URIRef, term
from rdflib.namespace import XSD
from rdflib.namespace import DC, FOAF
from collections import defaultdict
from haversine import haversine, Unit
from queue import PriorityQueue
from Map_Helpers import *
print('testing A* search with a priority queue')

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

# search using the A* algorithm.
startNode = musina
goalNode = bethlehem

openNodes = PriorityQueue()
parents = {}    # we need to track the parents of each child node we find for the backtrack at the end
roadsofar = {}  # for the formula f(s) = g(s) + h(s) we need to use the cost so far as well as the heuristic cost
openNodes.put((haversine_distance(g, startNode, goalNode), startNode))
roadsofar[startNode] = 0
parents[startNode] = None
goal = False
while goal is False:
    if not openNodes.empty(): 
        (dist, activeNode) = openNodes.get()
        if activeNode == goalNode:
            goal = True
        else:
            children = connected_towns(g, activeNode, goalNode)
            for child in children:
                newroadlength = roadsofar[activeNode] + child[2]    # road so far is the road so far to the parent and road length
                if child[0] not in roadsofar or newroadlength < roadsofar[child[0]]:
                    parents[child[0]] = activeNode
                    roadsofar[child[0]] = newroadlength      
                    openNodes.put((roadsofar[child[0]] + child[1], child[0])) # add the haversine and road so far to the priority queue
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