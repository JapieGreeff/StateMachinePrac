import rdflib
from rdflib import URIRef
from rdflib.namespace import RDF, FOAF

print(RDF.type)
print(FOAF.knows)

g=rdflib.Graph()
g.load('http://dbpedia.org/resource/North-West_University')

for s,p,o in g:
    if p == URIRef('http://www.w3.org/1999/02/22-rdf-syntax-ns#type'):
        print(s,p,o)