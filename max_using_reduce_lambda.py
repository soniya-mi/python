import functools;
list = [2,3,6,1]
print (functools.reduce(lambda a,b : a if a > b else b , list))