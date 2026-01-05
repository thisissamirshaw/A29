#WAP to check whether a data is SVDT or MVDT
a=input("enter any data")
if len(a)==1:
    print("SVDT")
else:
    print("MVDT")

    data=eval(input("enter any data"))
    if type(data) in [int,float,complex,str,bool]:
        print("SVDT")