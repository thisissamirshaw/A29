#WAP
a='Hai Hello'.split()
op={'Hai':['Hai',6,'iaH3'],'Hello':['Hello',10, 'olleH10']}
out={}
i=0
while i<len(a):
    out[a[i]]=[a[i],len(a[i])*2,a[i][::-1]+str(len(a[i]))]
    i+=1
print(out)