import rdflib
from rdflib import URIRef
from rdflib.namespace import RDF, FOAF
#import pickle

# pip install rdflib
# documentation on rdflib:
# https://rdflib.readthedocs.io/en/stable/
# https://rdflib.readthedocs.io/en/stable/gettingstarted.html
# https://rdflib.readthedocs.io/en/stable/intro_to_parsing.html
# https://rdflib.readthedocs.io/en/stable/intro_to_graphs.html

# 'http://dbpedia.org/resource/University_of_Johannesburg'
# 'http://dbpedia.org/resource/University_of_the_Witwatersrand'

univ_graph = rdflib.Graph()
univ_graph.load(URIRef('http://dbpedia.org/resource/North-West_University'))
univ_graph.load(URIRef('http://dbpedia.org/resource/University_of_Johannesburg'))


# writing a scraped graph to a file as an object
#sessionfile = open('./nwugraph.pkl', 'wb') # write binary
#pickle.dump(univ_graph, sessionfile)
#sessionfile.close()

# writing a graph to a n3 file
#univ_graph.serialize(destination='./univ.nt', format='nt')

# reading a graph object back out of a pickled file
# sessionfile = open('./nwugraph.pkl', 'rb')
# testgraph = pickle.load(sessionfile)

# reading single values from the graph 
chancellor = testgraph.value(subject=URIRef('http://dbpedia.org/resource/North-West_University'), predicate=URIRef('http://dbpedia.org/ontology/chancellor'))
vicechancellor = testgraph.value(subject=URIRef('http://dbpedia.org/resource/North-West_University'), predicate=URIRef('http://dbpedia.org/ontology/viceChancellor'))
print(chancellor)
print(vicechancellor)

# reading a list of values from the graph
cities = list(testgraph.objects(subject=URIRef('http://dbpedia.org/resource/North-West_University'), predicate=URIRef('http://dbpedia.org/ontology/city')))
for value in cities:
    print(value)

