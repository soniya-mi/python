class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
    
    def traverse(self):
        node=self
        while node != None:
            print node.val
            node=node.next
    
    def size(self):
        node=self
        count =0 
        while node != None:
            count = count + 1
            node=node.next
        return count
        
    def swap(self,n):
    	node=self
    	node1=self
    	node2=self
    	size_of_ll = node.size()
    	elem=(size_of_ll+1) - n 
    	#print size_of_ll  ,  elem , n
    	index = 0
    	while node != None:
    		index = index + 1
    		if index == n:
    			node1 = node
    		elif index == elem:
    			node2 = node
    		node=node.next
    	
    	tmp = node1.val
    	node1.val = node2.val
    	node2.val = tmp
        
        
node1 = Node(12)
node2 = Node(99)
node3 = Node(37)
node4 = Node(1)
node5 = Node(9)
node6 = Node(3)
node7 = Node(2)
node8 = Node(89)
node9 = Node(7)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7
node7.next = node8
node8.next = node9

#node1.traverse()
n = 3
print "\n"
print "\n"
node1.swap(n)
node1.traverse()