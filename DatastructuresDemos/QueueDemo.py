from queue import Queue

# create an empty queue
myQueue = Queue()

# append to the queue - this is equivalent to enqueue
myQueue.put('a')
myQueue.put('b')
myQueue.put('c')
myQueue.put('d')
myQueue.put('e')
myQueue.put('f')

# loop over 7 times to get out each of the values we have enqueued onto the queue
for i in range(0,7):
    try:
        # Queue is synchronised - so multiple threads can enqueue and dequeue things. by default if the queue is empty when get is called it waits.
        # if block is set to false then the empty error will be raised when get is called on an empty queue
        print(f'{i}: {myQueue.get(block=False)}')
    except:
        print(f'{i}: the queue was empty')