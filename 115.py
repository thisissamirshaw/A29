#WAP to declare a function to count the number of digits
def countdts():
    num=int(input("enter a number"))
    if num<0: #handle negative number
        num=-num
        #Special case for 0
    elif num==0:
        count=1
    else:
        count=0
        while num>0:
            count+=1
            num//=10
        return ("Number of digits=", count)
print(countdts())
