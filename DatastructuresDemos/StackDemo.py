# create an empty list which will be our stack
myStack = []

# append to the stack - this is equivalent to "push"
myStack.append('a')
myStack.append('b')
myStack.append('c')
myStack.append('d')
myStack.append('e')
myStack.append('f')

# loop over 7 times to pop out each of the values we have pushed onto the stack
for i in range(0,7):
    try:
        print(f'{i}: {myStack.pop()}')
    except:
        print(f'{i}: the list was empty')
