def remove_spaces(dictionary):
    for key in dictionary.keys():
        list=key.split( )
        s = ""
        print s.join(list)
dictionary = {'key 1': 1, 'key 2': 2, 'key 3': 3 }
remove_spaces(dictionary)