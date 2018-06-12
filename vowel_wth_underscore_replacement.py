string="soniy agrawal"
expected_str=""
for char in string:
    if  char == "a" or char == "e" or char == "i" or char == "o" or char == "u" : 
        expected_str = expected_str + "_"
    else:
        expected_str = expected_str + char

print expected_str