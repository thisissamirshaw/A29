#WAP to check  whether a collection is homogeneous or heterogeneous
a=[1,'jkl']
if type(a[0])==type(a[1]):
    print("homogeneous")    
else:
    print("heterogeneous")