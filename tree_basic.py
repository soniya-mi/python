class BinaryTree():
    def __init__(self,value):
        self.value=value
        self.left_child=None
        self.right_child=None
	
	def insert_left(self,value):
		if self.left_child == None:
			self.left_child=BinaryTree(value)
		else:
			new_node=BinaryTree(value)
			new_node.left_child=self.left_child
			self.left_child=new_node
	
	def insert_right(self,value):
		if self.righ_child == None:
			self.right_child = BinaryTree(value)
		else:
			new_node=BinaryTree(value)
			new_node.right_child =self.right_child
			self.right_child=new_node
			
		
node = BinaryTree('a')
node.insert_left('b')
node.insert_right('c')

node_b=node.left_child
node_b.insert_left('d')

node_d=node_b.left_child
node_d.insert_left('e')

node_c=node.right_child
node_c.insert_left(f)





