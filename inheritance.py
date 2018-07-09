class parent_class:
    firstvar = "var1"
    secvar = "var2"

class child_class(parent_class):
    pass

pobj = parent_class()
cobj = child_class()
print cobj.firstvar
print cobj.secvar