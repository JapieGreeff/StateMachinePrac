class PriorityQueue(object):
    def __init__(self):
        self.dict = {}
    
    def __str__(self):
        stringrep = ""
        for k,v in self.dict.items():
            stringrep += f'{k}:{v}\n' 
        return stringrep

    def not_empty(self):
        return len(self.dict) > 0

    def push(self, key, value):
        self.dict[key] = value

    def pop(self):
        if len(self.dict) > 0:
            lowestValue = 9999
            lowestKey = None
            for k,v in self.dict.items():
                if v < lowestValue:
                    lowestValue = v
                    lowestKey = k
            del self.dict[lowestKey]
            return lowestKey, lowestValue
        else:
            return None

if __name__ == '__main__': 
    queue = PriorityQueue()
    queue.push('A', 1)
    queue.push('B', 3)
    queue.push('C', 2)
    queue.push('D', 5)
    queue.push('E', 4)

    print(queue.pop())
    print(queue.pop())
    print(queue.pop())
    print(queue.pop())
    print(queue.pop())