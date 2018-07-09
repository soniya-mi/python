def swap(Sample_string):

    new_string = ""
    for index in range(0,len(Sample_string)):
        if Sample_string[index] == '.':
            new_string = new_string + ','
        elif Sample_string[index] == ',':
            new_string = new_string + '.'
        else:
            new_string  = new_string + Sample_string[index]
            continue

    print new_string

Sample_string = '32.054,23'
swap(Sample_string)