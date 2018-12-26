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
			#prev = slowPtr
			slowPtr = slowPtr.next
		return slowPtr

	def reverse(self,ptr):
		prev = None
		curr = ptr
		while curr is not None:
			nextNode = curr.next
			curr.next = prev
			prev = curr
			curr = nextNode
		self.head = prev

	def pelindromeCheck(self):
		curr = self.head
		mid = self.middleNode()
		print(mid.data)
		self.reverse(mid)
		self.display()
		

	

if __name__ == '__main__':
	l = linkedList()
	l.append('a')
	l.append('b')
	l.append('c')
	l.append('d')
	l.append('e')
	l.append('f')
	l.display()
	print(l.pelindromeCheck())
	#l.display()
