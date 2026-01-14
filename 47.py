#WAP to extract vowels from a str and count vowels
a=input("enter a str")
out=''
i=0
count=0
while i<len(a):
    if a[i] in "AEIOU": #membership operators
        out+=a[i]    #we are adding to an empty string
        count+=1
    i+=1    
print(out)
print(count)