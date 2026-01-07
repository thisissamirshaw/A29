#WAP to do the following:
a=['hai',3+5j, 3,3,'hai',9.8]
op=['hai',3+5j,3,9.8]
out=[]
i=0
while i<len(a):
    if a[i] not in out:
        out.append(a[i])
    i+=1
print(out)        

