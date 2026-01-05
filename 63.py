# a='aabcbcdcbab'
#op='a3b4c3d1'
#WAP to count the no of same characters in a string and give the output as above
a='aabcbcdcbab'
i=0
out=''
while i<len(a):
    if a[i] not in out:
        out+=a[i]+str(a.count(a[i]))
    i+=1
print(out)    

