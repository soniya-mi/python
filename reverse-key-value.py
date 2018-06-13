#!/usr/bin/python
dict = { "key1" : 1 , "key2" : 2 , "key3" : 3 }

for key in dict.keys():
    tmp = dict[key]
    del dict[key]
    dict[tmp] = key
    key = tmp
    

print dict