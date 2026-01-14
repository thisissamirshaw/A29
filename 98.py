# #WAP to check the number is prime.
num=int(input("Enter a number: "))
for i in range(2,num):
    if num%i==0:
        print("Not prime")
        break
else:
    print("prime number")   