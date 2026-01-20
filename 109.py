#WAP 
def replitt():
    a='10100$10!0110'
    o='10100#10#0110'
    out=''
    for i in range(len(a)):
        if a[i] in ('$','!'):
            out+='#'
        else:
            out+=a[i]
    print(out)
replitt()            

