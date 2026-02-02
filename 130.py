#WAP 
def fact(n):
    if n==0 or n==1:
        return 1
    return n*fact(n-1)
def exfact():
    out=[]
    for i in range(1,11):
        out+=[fact(i)]
    return out
print(exfact())
