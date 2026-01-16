#WAP extract int from a list, it should be palindrome and at even index
a=list(eval(input("enter a list")))
out=[]
for i in a:
    if not (type(i)==int or int(a.index(i))%2==0 or str(i)[::-1]==str(i)):
        continue
    out+=[i]
print(out)

        