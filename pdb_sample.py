def area (w,h):
    import pdb
    pdb.set_trace()
    a = w*h
    print a
    cal_perimeter(w,h)

def cal_perimeter(w,h):
    p = 2 * (w+h)
    print p

area(10,20)

#enter into another screen where program output is seen
# n -> repeat  previous command
# p -> p variable name , emaple p w , p h , displays values of these variables
# l -> will tell you on which lilne you are
# q -> quit
# c -> continue
# r -> return from function
# b -> in the pdb prompt , wite b line_num and enter say "c" after that , and keep typing "n" , example : b 10 (enter) ,
#       c and then press n it will gi
ve 60 (10+20) * 2