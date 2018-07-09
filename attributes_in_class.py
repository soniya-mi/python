class parent_class1(object):
    var1 = "hello"
    def func(self):
        print "this is in class 1"

class parent_class2(object):
    def func(self):
        print "this is in class 2"

class child_class(parent_class1,parent_class2):
    def func(self):
        super(child_class,self).func()

cobj = child_class()

print hasattr(cobj,'var1')
print hasattr(cobj,'func')

if hasattr(cobj,'func'):
    print "attribute found"

setattr(cobj, 'var2' , "value me")
print hasattr(cobj,'var2')
#delattr(cobj,'var2')


print getattr(cobj,'var2')