# testing greedy algorithm with a priority queue
# using https://pypi.org/project/haversine/ for distances

import random
from rdflib import Graph, Literal, BNode, Namespace, RDF, URIRef, term
from rdflib.namespace import XSD
from rdflib.namespace import DC, FOAF
from collections import defaultdict
from haversine import haversine, Unit
from queue import PriorityQueue
from Map_Helpers import *

print('testing Best first (Greedy) search with a priority queue')

g = Graph()

# adding in all of the town nodes
musina = add_town(g, 'Musina', -22.338056, 30.041667)
polokwane = add_town(g, 'Polokwane', -23.9, 29.45)
modimolle = add_town(g, 'Modimolle', -24.7, 28.406111)
mbombela = add_town(g, 'Mbombela', -25.465833, 30.985278)
emalahleni = add_town(g, 'Emalahleni', -25.876583, 29.200972) # previously Witbank
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
kimberley = add_town(g,'Kimberley',-28.7282,24.7499)
ladysmith = add_town(g,'Ladysmith',-28.5597,29.7808)

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

# search using the Best first (greedy) approach. As we are using a cyclic graph we need to have a closed list too
startNode = musina
goalNode = bethlehem

openNodes = PriorityQueue()
closedNodes = []
parents = {}
openNodes.put((haversine_distance(g, startNode, goalNode), startNode) )
parents[startNode] = None
goal = False
while goal is False:
    if not openNodes.empty(): 
        #print(f'open: {openNodes.queue}, closed: {closedNodes}\n')
        value = openNodes.get()
        dist = value[0]
        activeNode = value[1]
        closedNodes.append(activeNode)
        if activeNode == goalNode:
            goal = True
        else:
            children = connected_towns(g, activeNode, goalNode)
            for child in children:
                if child[0] not in closedNodes:
                    openNodes.put((child[1], child[0]))    # append the child node as well as it's haversine distance to the goal
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
    for node in reversed(backtrackpath):
        print(node)
else:
    print('no path could be found!')

print(f'A-K {haversine_distance(g, vryburg, standerton)}')
print(f'B-K {haversine_distance(g, mahikeng, standerton)}')
print(f'C-K {haversine_distance(g, klerksdorp, standerton)}')
print(f'D-K {haversine_distance(g, rustenburg, standerton)}')
print(f'E-K {haversine_distance(g, pretoria, standerton)}')
print(f'F-K {haversine_distance(g, vereeniging, standerton)}')
print(f'G-K {haversine_distance(g, kroonstad, standerton)}')
print(f'H-K {haversine_distance(g, bloemfontein, standerton)}')
print(f'I-K {haversine_distance(g, kimberley, standerton)}')
print(f'J-K {haversine_distance(g, bethlehem, standerton)}')
print(f'K-K {haversine_distance(g, standerton, standerton)}')
print(f'L-K {haversine_distance(g, emalahleni, standerton)}')
print(f'M-K {haversine_distance(g, mbombela, standerton)}')
print(f'N-K {haversine_distance(g, ladysmith, standerton)}')
