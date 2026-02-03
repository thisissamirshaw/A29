#WAP to check whether a data is SVDT or MVDT
data=eval(input("enter any data"))
if type(data) in [int,float,complex,str,bool]:
    print("SVDT")
else:
    print("MVDT")