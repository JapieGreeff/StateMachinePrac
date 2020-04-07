import random
from rdflib import Graph, Literal, BNode, Namespace, RDF, URIRef, term
from rdflib.namespace import XSD
from rdflib.namespace import DC, FOAF
from collections import defaultdict
from haversine import haversine, Unit
from queue import PriorityQueue

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