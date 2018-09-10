def decorate_name(f):
    def inner():
        print "Name:"
        f()
    return inner

def print_name():
    print "Minal"

r=decorate_name(print_name)
r()

==========================================================

def decorate_name(f):
    def inner():
        print "Name:"
        f()
    return inner

#decorator function
@decorate_name
def print_name():
    print "Minal"

print_name()

==========================================================

def decorate_wth_cheese(f):
    def inner():
        f()
        print "with cheese"
    return inner

def decorate_wth_topping(f):
    def inner():
        f()
        print "with topping"
    return inner 

 
def base_pizza():
    print "i am base"

d = decorate_wth_cheese(base_pizza)
d = decorate_wth_cheese(d)
d = decorate_wth_topping(d)
d()


===============================================================

def math(f):
    def inner(a,b):
        return 2*(f(a,b))
    return inner
    
@math      
def add(x,y):
    return x+y
    
print add(9,10)

