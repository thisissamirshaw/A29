#WAP LIST REC
def ex_fact(a,i=0,out=[]):
    def fact(n):
        if n==0 or n==1:
            return 1
        return n*fact(n-1)
    if i>=len(a):
        return out
    else:
        out+=[fact(a[i])]
        return ex_fact(a,i+1,out)
print(ex_fact([4,5,8]))