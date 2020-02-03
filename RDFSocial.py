import random
from rdflib import Graph, Literal, BNode, Namespace, RDF, URIRef
from rdflib.namespace import DC, FOAF
from collections import defaultdict


def create_person(graph, name, surname):
    #print(f'{name} {surname}')
    person = BNode()
    graph.add( (person, RDF.type, FOAF.Person) )
    graph.add( (person, FOAF.familyName, Literal(surname)) )
    graph.add( (person, FOAF.givenName, Literal(name)) )
    graph.add( (person, FOAF.name, Literal(f'{name} {surname}')) )
    graph.add( (person, FOAF.mbox, Literal(f'{name}_{surname}@example.com')) )

def create_friendship(graph, personA, personB):
    if (personA, FOAF.knows, personB) not in graph:
        graph.add( (personA, FOAF.knows, personB) )
        graph.add( (personB, FOAF.knows, personA) )

def get_recommendations(graph, person):
    friends = list(graph.objects(person, FOAF.knows))
    recommendations = defaultdict(int)
    for friend in friends:
        for foaf in list(graph.objects(friend, FOAF.knows)):
            if foaf not in friends and foaf is not person:
                foafname = graph.value(subject=foaf, predicate=FOAF.name)
                recommendations[foafname] += 1
    return recommendations

names = []
surnames = []
with open('names.txt') as namefile:
    names = namefile.read().splitlines() 
with open('surnames.txt') as surnamefile:
    surnames = surnamefile.read().splitlines() 

g = Graph()

# create 50 random people
for _ in range(50):
    create_person(g, random.choice(names), random.choice(surnames))

# get a list of all the people
people = list(g.subjects(RDF.type, FOAF.Person))

# create 150 random friendships
for _ in range(150):
    personA = random.choice(people)
    personB = random.choice(people)
    while personB is personA:
        personB = random.choice(people)
    create_friendship(g, personA, personB )

# print the list of friends for each person
for person in people:
    name = g.value(subject=person, predicate=FOAF.name)
    friends = list(g.objects(person, FOAF.knows))
    print(f'{name} is friends with:')
    for friend in friends:
        friendsname = g.value(subject=friend, predicate=FOAF.name)
        print(f'{friendsname}')
    print('')

# get a list of friends of friends, and then remove all people I am already friends with   
for person in people:
    recommendations = get_recommendations(g, person)
    name = g.value(subject=person, predicate=FOAF.name)
    print(f'I recommend to {name}:')
    for potentialfriend in sorted(recommendations, key=recommendations.get, reverse=True):
        print(f'{potentialfriend}:{recommendations[potentialfriend]}')
    print()

# *** you can style this output much better, but the idea is there.
# links to remember:
# https://rdflib.readthedocs.io/en/stable/
# http://xmlns.com/foaf/spec/
# https://www.w3.org/1999/02/22-rdf-syntax-ns

# *** consider whether the set operations on graphs will be useful in doing the friend of friend stuff
# https://rdflib.readthedocs.io/en/stable/intro_to_graphs.html

print(FOAF.knows)
print(RDF.type)

g.serialize(destination='output.txt', format='nt')
