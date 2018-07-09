class parent_class1:
    firstvar = "var1"
    secvar = "var2"


class parent_class2:
    thirdvar = "var3"
    secvar = "var4"

# execution happens based on how classes are defined in list while the third class is declared.
# if we "class child_class(parent_class2,parent_class1):" then class2 will be looked first

class child_class(parent_class1,parent_class2):
    pass

cobj = child_class()

print cobj.secvar