class stack ():
    def __init__(self):
        self.stack = []

    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.stack.pop()

    def push(self, val):
        return self.stack.append(val)

    def size(self):
        return len(self.stack)

    def is_empty(self):
        return self.size() == 0
    
    def top(self):
        length = self.size()
        return self.stack[length-1]

def balance_check(str):
    s = stack()
    bal = True
    index = 0
    while index < len(str) and bal:
        sym = str[index]
        if sym == "(" or sym == "{":
            s.push(sym)
        else:
            if s.is_empty():
                bal = False
            else:
                v = s.top()
                if v =="(" and sym == ")" or v =="{" and sym == "}":
                    s.pop()
                else:
                    bal = False
        index = index + 1
    if bal and s.is_empty():
        return True
    else:
        return False

str = '({)}'
print (balance_check(str))
