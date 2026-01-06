#WAP 
a='How are you all'
op='How_are_you_all'
out=''
i=0
while i<len(a):
    if 'a'<=a[i]<='z':
        out+=chr(ord(a[i])-32)
    elif(a[i]==' '):
        out+='_'
    else:
        out+=a[i];
    
    i+=1
print(out) 