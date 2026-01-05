#WAP to find greatest among three using nested if
a=int(input("enter the 1st no"))
b=int(input("enter the 2nd no"))
c=int(input("enter the 3rd no"))
if(a>b) and (a>c):
    print(a)
elif b>c:
    print(b)
else:
    print(c)