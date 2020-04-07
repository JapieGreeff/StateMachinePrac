import random

# creates a list of nodes that can be used for best first search and shuffles the cost for each of them (for exam generation)

def char_range(c1, c2):
    """Generates the characters from `c1` to `c2`, inclusive."""
    for c in range(ord(c1), ord(c2)+1):
        yield chr(c)

characters = list(char_range('a', 'p'))
values = list(range(1,(len(characters)+1)))
random.shuffle(values)9


for c in characters:
    print(c, values.pop())
