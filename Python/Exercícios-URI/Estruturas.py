import queue
import heapq

class MyPriorityQueue(object):
    def __init__(self):
        self.Data=[]
    def put(self,value):
        self.Data.append(value)
        heapq.heapify(self.Data)
    def pop(self):
        if not self.is_empty():
            return self.Data.pop()
    def is_empty(self):
        return len(self.Data)==0

if __name__ == "__main__":
    q = MyPriorityQueue()
    q.put(5)
    q.put(9)
    q.put(1)
    q.put(3)
    print(q.Data)
    while not q.is_empty():
        print(q.pop())

  
    
    '''while q.empty() is False:
        #q.queue.sort(reverse=True)
        e=q.get()
        print(e[1])'''