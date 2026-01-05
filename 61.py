#WAP to input any three digit number and print sum of its digits
a=int(input("enter a three digit number"))
sum=0
i=0
while i<3:
    sum+=a%10
    a=a//10
    i+=1
print(sum)    