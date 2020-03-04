import rdflib
from rdflib import URIRef
from rdflib.namespace import RDF, FOAF


nwu_graph = rdflib.Graph()
uj_graph = rdflib.Graph()
wits_graph = rdflib.Graph()
nwu_graph.parse('text.n3', format='n3')
#nwu_graph.load(URIRef('http://dbpedia.org/resource/North-West_University'))
#uj_graph.load(URIRef('http://dbpedia.org/resource/University_of_Johannesburg'))
#wits_graph.load(URIRef('http://dbpedia.org/resource/University_of_the_Witwatersrand'))

chancellor_predicate = URIRef('http://dbpedia.org/ontology/chancellor')

print(nwu_graph.value(subject=URIRef('http://dbpedia.org/resource/North-West_University'), predicate=URIRef('http://dbpedia.org/ontology/chancellor')))
#nwu_graph.serialize(destination='text.n3',format='n3')

#print(RDF.type)
#print(FOAF.knows)
#for s,p,o in g:
    #if p == URIRef('http://dbpedia.org/ontology/chancellor'):
    #    print(s,p,o)    
    #if p == RDF.type:
    #    print(s,p,o)    
    #if p == URIRef('http://www.w3.org/1999/02/22-rdf-syntax-ns#type'):
    #    print(s,p,o)