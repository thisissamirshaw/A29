#WAP

op='Python'
def cappp():
    a='python'
    out=''
    for i in range(len(a)):
        if i==0 and 'a'<=a[i]<='z':
            out+=chr(ord(a[i])-32)
        else:
            out+=a[i]
    print(out)     
cappp()       

    