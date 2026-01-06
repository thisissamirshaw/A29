#WAP to produce with space
a='hai hello@'
op='HAIHELLO'
out=''
i=0
while i<len(a):
    if 'a'<=a[i]<='z':
        out+=chr(ord(a[i])-32)
    elif(a[i]==' '):
        out+=' '
    else:
        out+=a[i];
    
    i+=1
print(out) 