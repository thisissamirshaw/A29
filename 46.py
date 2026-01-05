#WAP to extract vowels from a str
a=input("enter a str")
out=''
i=0
while i<len(a):
    if a[i] in "AEIOU":
        out+=a[i]
    i+=1    
print(out)
