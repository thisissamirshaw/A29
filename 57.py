#WAP to take a="Python is very easy " print as dict O/P={'python': 'nohtpy', 'is': 'si', 'very': 'yrev', 'easy': 'ysae'}
#Theory on variable.split()
#Converts into a list of str example: ['I','love','Python']
a="python is very easy"
a=a.split()
i=0
out={}
while i<len(a):
    out[a[i]]=a[i][::-1]
    i+=1
print(out)    



