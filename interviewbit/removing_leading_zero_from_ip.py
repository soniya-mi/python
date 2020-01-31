
Input="100.020.003.400"
ip_list=Input.split(".")
new_ip=""

for octate in ip_list:
    new_int=int(octate)
    str_oct=str(new_int)
    if new_ip == "":
        new_ip=str_oct
    else:
        new_ip=new_ip+"."+str_oct

print new_ip

