#WAP Take a list using eval().If it is homogeneous, then check:if elements are int → print "All integers" else → print "All same type but not int"Else → "Heterogeneous list"
li_st = eval(input("Enter a list: "))

if type(li_st) is list:
    if all(type(item) == type(li_st[0]) for item in li_st):
        if type(li_st[0]) is int:
            print("All integers (Homogeneous int list)")
        else:
            print("All same type but not int")
    else:
        print("Heterogeneous list")
else:
    print("Not a list")
