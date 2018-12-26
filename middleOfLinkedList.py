class node:
	def __init__(self,data=None):
		self.data = data
		self.next = None

class linkedList:
	def __init__(self):
		self.head = None
		self.length = 0
	def append(self, n):
		newNode = node(n)
		if self.length == 0:
			self.head = newNode
		else:
			curr = self.head
			while curr.next is not None:
				curr = curr.next
			curr.next = newNode
		self.length += 1
	def display(self):
		curr = self.head
		d = []
		while curr is not None:
			d.append(curr.data)
			curr = curr.next
		print(d)
	def middleNode(self):
		slowPtr = self.head
		fastPtr = self.head
		while fastPtr is not None and fastPtr.next is not None:
			fastPtr = fastPtr.next.next
			slowPtr = slowPtr.next
		print(slowPtr.data)
	def countOfNodeData(self,n):
		curr = self.head
		count = 0
		while curr is not None:
			if curr.data == n:
				count += 1
			curr = curr.next
		return count
	def countNodeRecursive(self,ptr, n):
		if ptr is None:
			return 0
		if ptr.data == n:
			#print(ptr.data)
			return 1 + self.countNodeRecursive(ptr.next,n)
		return self.countNodeRecursive(ptr.next,n)

if __name__ == '__main__':
	l = linkedList()
	l.append(1)
	l.append(2)
	l.append(1)
	l.append(2)
	l.append(1)
	l.append(3)
	l.append(1)
	#l.middleNode()
	#l.countOfNodeData(1)

	#print(l.countOfNodeData(1))

	print(l.countNodeRecursive(l.head,1))