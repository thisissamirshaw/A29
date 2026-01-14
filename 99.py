# #WAP to check a list is homogeneous or hetrogeneous.
a=[1,2,3,4]
for i in a :
    if type(a[0])!=type(a[i]):
        print("hetrogeneous")
        break
else:
    print("homogeneous") 