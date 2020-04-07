import rdflib
from rdflib import URIRef
from rdflib.namespace import RDF, FOAF
import pickle

univ_graph = rdflib.Graph()
univ_graph.load(URIRef('http://dbpedia.org/resource/Category:Public_universities_in_South_Africa'))

univ_graph.serialize(destination='./univ.nt', format='nt')

universities = list(univ_graph.subjects(object=URIRef('http://dbpedia.org/resource/Category:Public_universities_in_South_Africa'), predicate=URIRef('http://purl.org/dc/terms/subject')))
for value in universities:
    univ_graph.load(value)
    #label = univ_graph.value(subject=URIRef(value), predicate=URIRef('http://www.w3.org/2000/01/rdf-schema#label'))
    label = univ_graph.preferredLabel(subject=URIRef(value), lang='en')[0][1]
    chancellor = univ_graph.value(subject=URIRef(value), predicate=URIRef('http://dbpedia.org/ontology/chancellor'))
    vicechancellor = univ_graph.value(subject=URIRef(value), predicate=URIRef('http://dbpedia.org/ontology/viceChancellor'))
    print(f'{label}: {chancellor}, {vicechancellor}')