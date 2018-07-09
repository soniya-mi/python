class exampleClass:
    var1 = "this is var one"
    var2 = "this is var two"
    def class_method(self):
        print "i am class method"

class_obj = exampleClass()
print class_obj.var1
print class_obj.var2
class_obj.class_method()