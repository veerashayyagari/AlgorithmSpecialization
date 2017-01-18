# python3

import sys, threading
from collections import deque

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class Node:
    def __init__(self,val):
        self.value = val
        self.children = [] 
        self.level = 0       

    def addChildren(self,node):
        self.children.append(node)

    def hasChildren(self):
        return (len(self.children) > 0)

class Tree:
        def __init__(self):
            self.root = None
            self.height = 0            

        def read(self):
            self.n = int(sys.stdin.readline())
            self.parent = list(map(int, sys.stdin.readline().split()))

        def build_tree(self):
            nodes = [Node(i) for i in range(self.n)]

            for idx,next in enumerate(self.parent):
                if next == -1:   
                    nodes[idx].level = 1                                   
                    self.root = nodes[idx]                    
                else:                    
                    nodes[next].addChildren(nodes[idx])

        def compute_height(self):
            if self.root is None:
                return

            self.height = 1
            queue = deque()

            for child in self.root.children:
                child.level = 2
                queue.append(child)

            while len(queue) > 0:
                node = queue.popleft()
                self.height = max(self.height,node.level)
                for child in node.children:
                    child.level = node.level + 1
                    queue.append(child)


        def compute_height_recursive(self,node=None):
            if node is None:
                node = self.root

            if node.hasChildren() == False:
                return 1

            height = 0
            for child in node.children:
                height = max(height,self.compute_height_recursive(child))

            return height+1


def main():
  tree = Tree()
  tree.read()
  tree.build_tree()
  tree.compute_height()
  print(tree.height)

threading.Thread(target=main).start()
