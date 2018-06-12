import functools
list = [4,3,2,1]
print (functools.reduce(lambda a,b : a if a < b else b , list))