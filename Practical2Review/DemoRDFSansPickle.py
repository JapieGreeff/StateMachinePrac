import rdflib
from rdflib import URIRef
from rdflib.namespace import RDF, FOAF
import pickle

# pip install rdflib
# documentation on rdflib:
# https://rdflib.readthedocs.io/en/stable/
# https://rdflib.readthedocs.io/en/stable/gettingstarted.html
# https://rdflib.readthedocs.io/en/stable/intro_to_parsing.html
# https://rdflib.readthedocs.io/en/stable/intro_to_graphs.html

# create a new graph
univ_graph = rdflib.Graph()

# load information from the knowledge base into the graph
univ_graph.load(URIRef('http://dbpedia.org/resource/North-West_University'))

# writing a graph to an nt file (text based version of the graph)
univ_graph.serialize(destination='./univ.nt', format='nt')

# reading single values from the graph 
print('querying single values from the graph')
chancellor = univ_graph.value(subject=URIRef('http://dbpedia.org/resource/North-West_University'), predicate=URIRef('http://dbpedia.org/ontology/chancellor'))
vicechancellor = univ_graph.value(subject=URIRef('http://dbpedia.org/resource/North-West_University'), predicate=URIRef('http://dbpedia.org/ontology/viceChancellor'))
univ = univ_graph.preferredLabel(subject=URIRef('http://dbpedia.org/resource/North-West_University'), lang='en')[0][1]
print(chancellor)
print(vicechancellor)
print(univ)

# reading a list of values from the graph
print('querying multiple values from the graph')
cities = list(univ_graph.objects(subject=URIRef('http://dbpedia.org/resource/North-West_University'), predicate=URIRef('http://dbpedia.org/ontology/city')))
for value in cities:
    print(value)

# reading a list of values where the university is the object in the semantic triple 
print('querying subjects where the university is the object in the semantic triple')
subjects = list(univ_graph.subjects(object=URIRef('http://dbpedia.org/resource/North-West_University'), predicate=URIRef('http://dbpedia.org/ontology/university')))
for subject in subjects:
    print(subject)

