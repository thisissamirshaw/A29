#WAP change a binary str from 0 to 1 and 1 to 0.
def ext(a,b):
    if len(a)==0 or len(b)==0:
        return abs(a.count('1')-b.count('1'))           
    return ext(abs(a.count('1')-b.count('1')))
print(ext('11001000111001','1010101010000')) 


def dif(a,b,out=0,c=0,c1=0,i=0):
    if i>=len(a) or i>=len(a):
        return out
    if a[i]=='1':
        c+=1
    if b[i]=='1':
        c1+=1
        out=c-c1
        return dif(a,b,out,c,c1,i+1)
    print(dif(111100010101))

