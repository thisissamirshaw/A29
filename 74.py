#WAP extract int from list which are palindrome in nature
a=[151,'stri','anna','magic','john',101,121,121,818,919]
i=0
out=[]
while i<len(a):
    if(type(a[i])==int):
        if str(a[i])==str(a[i])[::-1]:
            out+=[a[i]]
    i+=1
print(out)    

