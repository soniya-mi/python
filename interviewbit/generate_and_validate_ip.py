def is_valid(ip):
    # Splitting by "."
    ip = ip.split(".")

    # Checking for the corner cases
    for i in ip:
        if len(i) > 3 or int(i) < 0 or int(i) > 255:
            return False
        if len(i) > 1 and int(i) == 0:
            return False
        if len(i) > 1 and int(i) != 0 and i[0] == '0':
            return False
    return True

def convert(s):
    size = len(s)
    if size > 12:
        return {}
    snew = s
    l = []


    for i in range (1,size-2):
        for j in range(i+1, size - 1):
            for k in range(j+1, size):
                #print i , j , k

                snew = snew[:k] + "." + snew[k:]
                snew = snew[:j] + "." + snew[j:]
                snew = snew[:i] + "." + snew[i:]

                print snew
                if is_valid(snew):
                    l.append(snew)
                snew = s

    return l
A = "25525511135"
B = "25505011535"
print(convert(A))
#print(convert(B))
