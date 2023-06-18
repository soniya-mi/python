class stack():
    def __init__(self):
        self.stack =[]
    
    def pop(self):
        if self.is_empty():
            return None
        else:  
            return self.stack.pop()
            
    def push(self,elem):
        return self.stack.append(elem)
        
    def is_empty(self):
        return self.size() == 0
        
    def size(self):
        return len(self.stack)
        
    def print_stack(self):
        print (f"{self.stack}")
        
s = stack()
print (s.is_empty())
s.push(10)
s.push(20)
s.push(30)
s.print_stack()
print (s.pop())
s.push(40)
s.print_stack()
