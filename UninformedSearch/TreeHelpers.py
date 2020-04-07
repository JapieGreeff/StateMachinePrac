from rdflib import Graph, Literal, BNode, Namespace, RDF, URIRef
from rdflib.namespace import DC, FOAF

typeNode = Literal('Node')
typeEdge = Literal('Edge')
predParent = Literal('Parent')
predChild = Literal('Child')

class TreeHelpers:
    def __init__(self):
        pass

    def create_graph(self):
        return Graph()

    def add_node(self, graph, value):
        node = Literal(value) # can also be a BNode
        graph.add( (node, RDF.type, typeNode) )
        graph.add( (node, RDF.value, Literal(value)) )
        return node

    def create_child_relationship_by_value(self, graph, parentValue, childValue):
        parent = graph.value(predicate=RDF.value, object=Literal(parentValue))
        child = graph.value(predicate=RDF.value, object=Literal(childValue))
        if (parent, predChild, child) not in graph:
            graph.add( (parent, predChild, child) )
            graph.add( (child, predParent, parent) )

    def create_child_relationship(self, graph, parent, child):
        if (parent, predChild, child) not in graph:
            graph.add( (parent, predChild, child) )
            graph.add( (child, predParent, parent) )

    def get_children_by_value(self, graph, parentValue):
        parent = graph.value(predicate=RDF.value, object=Literal(parentValue))
        children = list(graph.objects(parent, predChild))
        return children

    def get_children(self, graph, parent):
        children = list(graph.objects(parent, predChild))
        return children

    def get_parent(self, graph, child):
        return graph.value(subject=child, predicate=predParent)

    def get_value(self, graph, node):
        return graph.value(subject=node, predicate=RDF.value)