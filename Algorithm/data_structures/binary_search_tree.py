class Node:
	def __init__(self,item):
		self.data=item 
		self.left=None
		self.right=None

class BST:
	def __init__(self):
		self.root=None

def search(root,item):
	if root==None:
		return False
	else:
		if item==root.data:
			return True
		elif item<root.data:
			return search(root.left, item)
		else:
			return search(root.right, item)
		


def insert_item(root,item):
	if root==None:
		root=Node(item)

	else:
		if item<root.data:
			root.left=insert_item(root.left,item)
			

		else:
			root.right=insert_item(root.right,item)
	
	return root

def print_inorder(root):
	if root==None:
		return

	elif root.left==None and root.right==None:
		print(root.data,end=' ')
	
	else:
		print_inorder(root.left)
		print(root.data,end=' ')
		print_inorder(root.right)

	return

#main program
root=None
for i in range(10):
	x=int(input())
	root=insert_item(root,x)

print_inorder(root)
print(search(root,4))
