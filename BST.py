class TreeNode:
	def __init__(self, val = 0, left = None, right = None):
		self.val = val
		self.left = left
		self.right = right

	
	def insert_element(self, root, new_val):
		if self.val < new_val:
			if root.right:
				self.insert_element(root.right, new_val)
			else:
				root.right = TreeNode(new_val, None, None)
				return self
		else:
			if root.left:
				self.insert_element(root.left, new_val)
			else:
				root.left = TreeNode(new_val, None, None)
				return self

	def print_tree(self,root, lst = []):

		if not root:
			return 
		self.print_tree(root.left,lst)
		lst.append(root.val)
		self.print_tree(root.right,lst)
		
		return lst
	def pretty_print(self, root, spacing = 5):
		char_dict = {'left':'/', 'right':'"\\"', 'space': ' '*spacing}

		print ([char for char in char_dict.values()])
		print("some spaces", " " *spacing, "ending")

	
def populate_tree():
	new_tree = TreeNode(4, None, None)
	root = new_tree
	new_tree.insert_element(root, 5)
	new_tree.insert_element(root, 6)
	new_tree.insert_element(root,3)
	new_tree.insert_element(root,1)
	new_tree.insert_element(root,7)
	return new_tree

#new_tree = new_tree.insert_element(3)


tree = populate_tree()
tree.pretty_print(tree)

#print(new_tree.print_tree(root))
#print('"\\"')



