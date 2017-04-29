# python3

import sys
import random

class Vertex:
	def __init__(self,key,count,left,right,parent):
		(self.key,self.count,self.left,self.right,self.parent) = (key,count,left,right,parent)

class Rope:
	def __init__(self, s):
		self.s = s
		self.root = None
		for c in s:
			new_vertex = Vertex(c,1,None,None,None)
			#self.initialize_node(new_vertex)
			self.root = self.merge(self.root,new_vertex)
			(rn,root) = self.find(self.root,random.randint(1,self.root.count))
			self.root = self.splay(rn)



		#print("Input Rope ->",self.inorder_debug(self.root))	



	def update(self,v):
		if v == None:
			return
		v.count = 1 + (v.left.count if v.left is not None else 0) + (v.right.count if v.right is not None else 0)
		if v.right is not None:
			v.right.parent = v
		if v.left is not None:
			v.left.parent = v

	def smallRotation(self,v):
		parent = v.parent
		if parent == None:
			return

		grandParent = v.parent.parent
		
		if parent.left == v:			
			m = v.right			
			v.right = parent			
			parent.left = m			
		else:
			m = v.left
			v.left = parent
			parent.right = m			

		self.update(parent)
		self.update(v)

		v.parent = grandParent
		
		if grandParent != None:
			if grandParent.left == parent:
				grandParent.left = v
			else:
				grandParent.right = v

	def bigRotation(self,v):
		parent = v.parent
		if parent == None:
			return

		# zig-zig
		if ((parent.left == v and parent.parent.left == parent) or \
			(parent.right == v and parent.parent.right == parent)):			
			self.smallRotation(parent)			
			self.smallRotation(v)			
		else:			
			self.smallRotation(v)			
			self.smallRotation(v)			


	def splay(self,v):
		if v == None:
			return		

		while v.parent != None:
			if v.parent.parent == None:				
				self.smallRotation(v)
				break

			#print("Big Rotation for {0} - {1}".format(v.key,v.count))
			self.bigRotation(v)			
		return v

	def find(self,root,count):
		v = root
		last = root
		#print('Finding {0}'.format(count))

		while (v != None):
			node_count = v.left.count if v.left is not None else 0
			last = v
			if count == node_count + 1:				
				break
			elif count < node_count + 1:				
				v = v.left
			else:								
				count = count - node_count - 1
				v = v.right

		#print('Found at {0}'.format(v.key))
		root = self.splay(last)		
		return (v,root)

	def split(self,root,count):
		#print("Splitting Root : {0} at Count : {1}".format(root.key,count))

		(right,base) = self.find(root,count)		

		if right is None:
			return (base,None)

		#print("After finding and splaying - {0} and {1}".format(right.key,right.count))
		#print(self.inorder_debug(right))

		left = right.left
		right.left = None
		if left is not None:
			left.parent = None

		self.update(left)
		self.update(right)
		return (left,right)

	def merge(self,left,right):
		if left is None:
			return right

		if right is None:
			return left

		while (right.left is not None):
			right = right.left

		#print("Printing Left ->")
		#self.inorder(left)

		#print("Right ->")
		#self.inorder(right)

		right = self.splay(right)
		right.left = left
		self.update(right)
		self.update(left)

		return right

	def insert(self,root,index,rope_to_insert):
		(left,right) = self.split(root,index)
		#print("Merge Left ->")
		#self.inorder_debug(left)

		#print("Merge Substring ->")
		#self.inorder_debug(rope_to_insert)
		root = self.merge(self.merge(left,rope_to_insert),right)
		return root

	def inorder(self,root,result):
		if root is None:
			return

		self.inorder(root.left,result)
		result.append(root.key)
		self.inorder(root.right,result)

	def inorder_norecursion(self,root,result):
		current = root
		stack = []
		complete = 0

		while not complete:
			if current is not None:
				stack.append(current)
				current = current.left
			else:
				if len(stack) > 0:
					current = stack.pop()
					result.append(current.key)

					current = current.right
				else:
					complete = 1		

	def inorder_debug(self,root):
		if root is None:
			return

		self.inorder_debug(root.left)
		print("Key -> {0} and Count -> {1}".format(root.key,root.count))
		self.inorder_debug(root.right)

	def inorder_traversal(self):
		result = []
		self.inorder_norecursion(self.root,result)
		return "".join(result)

	def result(self):				
		return self.s

	def process(self, i, j, k):
		(left,middle) = self.split(self.root,i+1)
		#print("After Left Middle Split")
		#print("Left ->")
		#print(self.inorder_debug(left))
		#print("Middle ->")
		#print(self.inorder_debug(middle))

		(middle,right) = self.split(middle,j-i+2)
		#print("After Middle Right Split")
		#print("Middle ->")
		#print(self.inorder_debug(middle))
		#print("Right ->")
		#print(self.inorder_debug(right))

		#print("Merging Left and Right")
		self.root = self.merge(left,right)
		#self.inorder_debug(self.root)


		#print("Inserting middle with Key {0} at {1}".format(middle.key,k+1))
		self.root = self.insert(self.root,k+1,middle)
		self.s = self.inorder_traversal()
		#print('After Processing ->',self.s)
		#self.inorder_debug(self.root)
                


rope = Rope(sys.stdin.readline().strip())

q = int(sys.stdin.readline())
for _ in range(q):
	i, j, k = map(int, sys.stdin.readline().strip().split())
	rope.process(i, j, k)
print(rope.result())
