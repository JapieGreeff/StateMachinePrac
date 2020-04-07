from queue import PriorityQueue

# create an empty priority queue
myPriorityQueue = PriorityQueue()

# append to the queue - each value appended also has a priority assigned to it in a two-tuple
myPriorityQueue.put((9.52, 'Alan'))
myPriorityQueue.put((9.31, 'Bob'))
myPriorityQueue.put((11.23, 'Carl'))
myPriorityQueue.put((10.47, 'Dan'))
myPriorityQueue.put((10.12, 'Evan'))
myPriorityQueue.put((10.59, 'Faf'))
myPriorityQueue.put((9.54, 'Gerald'))
myPriorityQueue.put((9.47, 'Hank'))

# loop over 9 times to get out each of the values we have enqueued onto the priority queue with their priority
for i in range(1,10):
    try:
        # Queue is synchronised - so multiple threads can enqueue and dequeue things. by default if the queue is empty when get is called it waits.
        # if block is set to false then the empty error will be raised when get is called on an empty queue
        priority, value = myPriorityQueue.get(block=False)
        print(f'{i}: {priority}, {value}')
    except:
        print(f'{i}: the queue was empty')