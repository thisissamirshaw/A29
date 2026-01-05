#WAP to check the number is even or odd, and also check is divisible by 5 or not
a=int(input("enter no"))
if a%2==0:
    print("even")
    if a%5==0:
        print("divisible by 5")
    else:
        print("not divisible by 5")