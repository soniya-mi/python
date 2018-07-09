class exampleClass:

    def __init__(self,name):
        print "in init function"
        self.name = name

    def set_name(self,name):
        self.name = name

    def get_name(self):
        return self.name

class_obj1 = exampleClass("soniya")
class_obj2 = exampleClass("aditya")


print class_obj1.get_name()
print class_obj2.get_name()