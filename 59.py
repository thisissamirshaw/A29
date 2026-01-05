#WAP to take a="Python is very easy " print as dict O/P={'python': 'nohtpy12', 'is': '4', 'very': 'yrev8', 'easy': '8'}
#Theory on variable.split()
#Converts into a list of str example: ['I','love','Python']
a="python is very easy"
a=a.split()
i=0
out={}
while i<len(a):
    if(i%2==0):
        out[a[i]]=a[i][::-1]+str(len(a[i])*2)
    else:
        out[a[i]]=len(a[i])*2
    i+=1
print(out) 