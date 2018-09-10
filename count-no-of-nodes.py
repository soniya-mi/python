class BinaryTree:
    count = 0
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None
	
    def insert_left(self, value):
        if self.left_child == None:
            self.left_child = BinaryTree(value)
        else:
            new_node = BinaryTree(value)
            new_node.left_child = self.left_child
            self.left_child = new_node
            
    def insert_right(self, value):
        if self.right_child == None:
            self.right_child = BinaryTree(value)
        else:
            new_node = BinaryTree(value)
            new_node.right_child = self.right_child
            self.right_child = new_node
   
    def pre_order(self):
        BinaryTree.count = BinaryTree.count + 1
        #print self.value
    
        if self.left_child:
            self.left_child.pre_order()
        
        if self.right_child:
            self.right_child.pre_order()
        
            #BinaryTree.count = BinaryTree.count + 1
            
        return BinaryTree.count
		

node = BinaryTree('1')
node.insert_left('2')
node.insert_right('3')

node_b=node.left_child
node_b.insert_left('4')
node_b.insert_right('5')

node_c=node.right_child
node_c.insert_left('6')

count = node.pre_order()
print count