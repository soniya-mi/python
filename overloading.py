class overloading():
    def __init__(self,var1,var2):
        self.var1 = var1
        self.var2 = var2

    def __str__(self):
        return "String representation of objet , overloaded"

    def __len__(self):
        return self.var1

    def __add__(self,var):
        self.var3 = self.var1 + var
        return self.var3

obj = overloading(10,20)
print obj
print len(obj)
print obj + 20