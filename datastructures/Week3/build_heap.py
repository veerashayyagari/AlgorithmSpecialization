# python3

class HeapBuilder:
  def __init__(self):
    self._swaps = []
    self._data = []

  def ReadData(self):
    n = int(input())
    self._data = [int(s) for s in input().split()]
    assert n == len(self._data)

  def WriteResponse(self):
    print(len(self._swaps))
    for swap in self._swaps:
      print(swap[0], swap[1])

  def SiftDown(self,i):
    leftChild = i*2 + 1
    rightChild = i*2 + 2
    length = len(self._data)
    while leftChild < length:      
      # store default min value to be left
      m = self._data[leftChild]

      # if right child is < length take min of left and right children
      if rightChild < length:
        m = min(self._data[rightChild],self._data[leftChild])

      # swap with the minimum of left or right, if that respective child
      # is greater than the parent which is i      
      if m == self._data[leftChild] and self._data[leftChild] < self._data[i]:
        self._swaps.append((i,leftChild))
        self._data[leftChild],self._data[i] = self._data[i],self._data[leftChild]
        i = leftChild
      elif rightChild < length and m == self._data[rightChild] and self._data[rightChild] < self._data[i]:
        self._swaps.append((i,rightChild))
        self._data[rightChild],self._data[i] = self._data[i],self._data[rightChild]
        i = rightChild
      else:
        # if parent is not greater than either left or right child, just traverse down
        i = leftChild

      leftChild = 2*i + 1
      rightChild = 2*i + 2


  def GenerateSwaps(self):
    size = len(self._data)

    if size > 1:
      for i in range(size//2,-1,-1):
        self.SiftDown(i)

    

  def Solve(self):
    self.ReadData()
    self.GenerateSwaps()
    self.WriteResponse()

if __name__ == '__main__':
    heap_builder = HeapBuilder()
    heap_builder.Solve()
