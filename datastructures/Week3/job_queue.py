# python3
class Node:
  def __init__(self,value,priority):
    self._value = value
    self._priority = priority

class BinaryMinHeap:
  def __init__(self,maxSize):
    self._data = [None]*maxSize
    self._maxSize = maxSize
    self._size = 0

  def siftDown(self,i):
    leftChild = 2*i + 1
    rightChild = 2*i + 2

    while leftChild < self._size:
      minIdx = leftChild

      if rightChild < self._size:
        if ((self._data[rightChild]._priority < self._data[leftChild]._priority) or
          (self._data[rightChild]._priority == self._data[leftChild]._priority and self._data[rightChild]._value < self._data[leftChild]._value)):

          minIdx = rightChild

      if ((self._data[minIdx]._priority < self._data[i]._priority) or
        (self._data[minIdx]._priority == self._data[i]._priority and self._data[minIdx]._value < self._data[i]._value)):

        self._data[minIdx],self._data[i] = self._data[i],self._data[minIdx]

      i = minIdx
      leftChild = 2*i + 1
      rightChild = 2*i + 2


  def siftUp(self,i):
    parentIdx = (i - 1)//2

    while parentIdx >= 0:

      if ((self._data[parentIdx]._priority > self._data[i]._priority) or 
        (self._data[parentIdx]._priority == self._data[i]._priority and self._data[parentIdx]._value > self._data[i]._value)):

        self._data[parentIdx],self._data[i] = self._data[i],self._data[parentIdx]

      i = parentIdx
      parentIdx = (i - 1)//2


  def insert(self,node):
    if self._size < self._maxSize:
      self._data[self._size] = node
      self._size += 1
      self.siftUp(self._size - 1)


  def extractMin(self):
    if self._size < 0 :
      return None

    result = self._data[0]
    self._data[0],self._data[self._size-1] = self._data[self._size-1],self._data[0]
    self._size -= 1
    self.siftDown(0)
    return result


  def printOut(self):
    for i in range(self._size):
      print("Printing out.., Value : {0} and Priority : {1}".format(self._data[i]._value,self._data[i]._priority))




class JobQueue:
    def read_data(self):
        self.num_workers, m = map(int, input().split())
        self.jobs = list(map(int, input().split()))
        assert m == len(self.jobs) 

    def assign_jobs(self):
        minHeap = BinaryMinHeap(self.num_workers)
        m = len(self.jobs)
        for i in range(m):
          if i < self.num_workers:
            node = Node(i,self.jobs[i])
            minHeap.insert(node)
            print(i,0)
          else:
            #minHeap.printOut()
            node = minHeap.extractMin()
            print(node._value,node._priority)
            newNode = Node(node._value,node._priority+self.jobs[i])
            minHeap.insert(newNode)

    def solve(self):
        self.read_data()
        self.assign_jobs()        

if __name__ == '__main__':
    job_queue = JobQueue()
    job_queue.solve()

