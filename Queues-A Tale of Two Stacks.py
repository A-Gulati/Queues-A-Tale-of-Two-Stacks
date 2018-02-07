#Queues-A-Tale-of-Two-Stacks
#https://www.hackerrank.com/challenges/ctci-queue-using-two-stacks/problem

class MyQueue(object):
    def __init__(self):
        self.first = [] #newest item is at the top of the stack
        self.second = [] #transfer items from first to second - top of this stack is where the oldest item is pushed to

    def transfer(self):
        if self.second == []: #dont need to transfer if second already has values
            for i in range(len(self.first)):
                self.second.append(self.first.pop()) #reverses order of first -> 2nd has oldest value at teh top

    def peek(self):
        self.transfer()
        return self.second[len(self.second)-1] #returns the last value in 2nd which is the oldest

    def pop(self):
        self.transfer()
        self.second.pop() #does this need to be returned?

    def put(self, value):
        self.first.append(value) #newest item is added to the end of first


queue = MyQueue()

t = int(raw_input())
for line in xrange(t):
    values = map(int, raw_input().split())

    if values[0] == 1:
        queue.put(values[1])
    elif values[0] == 2:
        queue.pop()
    else:
        print queue.peek()
