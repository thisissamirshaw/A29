#WAP to check the number is perfect number or not.
# eg 6, 1,2,3,6 factors, 1+2+3=6
n=int(input("enter a number"))
i=1
sum=0
while i<n:
    if(n%i==0):
        sum+=i
    i+=1   
if(sum==n):
    print("Perfect")
else:
    print("NOT")         
