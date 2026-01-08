#WAP a='((())))' op=1
a='((())))'
op=1
c=0
d=0
i=0
while i<len(a):
    if a[i]=='(':
        c+=1
    else:
        d+=1
    i+=1
                                                              
print((d-c))

