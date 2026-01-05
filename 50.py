#WAP to print num which are divisible by 5 between m and n
m = int(input("Enter a number:"))
n = int(input("Enter a number:"))
while m <= n:
    if m%5==0:
        print(m)
    m+=1  