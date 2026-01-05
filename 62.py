#WAP to print str from a given list which should have more than len 3 and should be in odd position of the list
a=['ab',321,9.8,'python',5+3j,'nike','just do it','abd']
#O/P=['python', 'nike']
out=[]
i=0
while i<len(a):
    if(type(a[i])==str and len(a[i])>3 and i%2!=0):
        out.append(a[i])
    i+=1
print(out)        

