`def gen():
    #print "once"
    yield 1
    
    #print "second"
    yield 2

a = gen()

for y in a:
    print y


