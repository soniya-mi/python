from itertools import permutations

permlist=permutations('ABC')


for item in permlist:
    print ''.join(item)
