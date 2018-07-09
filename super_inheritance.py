class parent_class1(object):
    def func(self):
        print "this is in class 1"

class parent_class2(object):
    def func(self):
        print "this is in class 2"

class child_class(parent_class1,parent_class2):
    def func(self):
        super(child_class,self).func()

cobj = child_class()

cobj.func()