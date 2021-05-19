

import heapq

class Stack(object):
    def __init__(self):
        self.Data=[]
    def insert(self,value):
        self.Data.append(value)
    def out(self):
        if not self.is_empty():
            return self.Data.pop()
    def is_empty(self):
        return len(self.Data)==0

class Queue(object):
    def __init__(self):
        self.Data=[]
    def insert(self,value):
        self.Data.append(value)
    def out(self):
        if not self.is_empty():
            return self.Data.pop(0)
    def is_empty(self):
        return len(self.Data)==0
     
class Priority(object):
    def __init__(self):
        self.Data=[]
    heapq.heapify(self.Data)
    def insert(self,value):
        self.Data.append(value)
    def out(self):
        if not self.is_empty():
            return self.Data.pop()
    def is_empty(self):
        return len(self.Data)==0
#main
if __name__ == "__main__":

