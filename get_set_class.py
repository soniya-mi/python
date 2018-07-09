class exampleClass:
    var1 = "this is var one"
    var2 = "this is var two"
    def set_name(self,name):
        self.name= name
    def get_name(self):
        return self.name

class_obj = exampleClass()
class_obj.set_name("soniya")
print class_obj.get_name()