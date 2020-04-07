from rdflib import Graph, Literal, BNode, Namespace, RDF, URIRef
from rdflib.namespace import DC, FOAF

class TreeHelpers:
    def __init__(self):
        pass

    def create_graph(self):
        return Graph()

    def add_node(self, graph, value):
        node = Literal(value) # can also be a BNode
        graph.add( (node, RDF.type, Literal('Node')) )
        graph.add( (node, RDF.value, Literal(value)) )
        return node

    def create_child_relationship(self, graph, parent, child):
        if (parent, Literal('Child'), child) not in graph:
            graph.add( (parent, Literal('Child'), child) )
            graph.add( (child, Literal('Parent'), parent) )

    def get_children(self, graph, parent):
        children = list(graph.objects(parent, Literal('Child')))
        return children

    def get_parent(self, graph, child):
        return graph.value(subject=child, predicate=Literal('Parent'))

    def get_value(self, graph, node):
        return graph.value(subject=node, predicate=RDF.value)