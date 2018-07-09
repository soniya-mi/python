def last_word(Input):
    list = Input.split(" ")
    word = list[len(list)-1]
    return len(word)

Input="Python Exercises"
print last_word(Input)