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
   
    def count_leaf_nodes(self):
        if self.left_child :
            self.left_child.count_leaf_nodes()
        if self.right_child : 
            self.right_child.count_leaf_nodes()
        elif self.left_child == None:
            BinaryTree.count = BinaryTree.count + 1
        return BinaryTree.count
    
    
    def count(self):
        left_count = 0
        right_count = 0
        #print left_count , right_count
        if self.left_child:
            left_count = self.left_child.count()
        if self.right_child:
            right_count = self.right_child.count()
        return 1 + left_count + right_count
            
        
        
        
        
node = BinaryTree('1')
node.insert_left('2')
node.insert_right('3')

node_b=node.left_child
node_b.insert_left('4')
node_b.insert_right('5')

node_c=node.right_child
node_c.insert_left('6')

count = node.count()
print count
