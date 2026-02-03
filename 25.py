#WAP to check whether a collection is homogeneous or heterogeneous
a=[1,'jkl']
if type(a[0])==type(a[1]):
    print("homogeneous")    
else:
    print("heterogeneous")

#WAP to check whether a collection is homogeneous or heterogeneous of any length
b=eval(input("enter any collection"))
out=type(b[0])
aut='homo'
for i in b:
    if type(i)!=out:
        aut='hetero'
        break
print(aut)    


