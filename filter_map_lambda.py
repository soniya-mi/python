#sample for map and filter 
def cube(x):
    return x*x*x
list = range(5)
print map(cube,list)
#filetr with lambda this can also be done on functions
print filter(lambda x : x%2 == 0,list)

#return vowel
str = "minal"
print filter(lambda char : char in "a|e|i|o|u" , str)
