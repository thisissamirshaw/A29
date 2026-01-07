#WAP 
a=['Hello','ab','Python',3+5j,'stan','apple',10]
#op={'Hello':10,'ab':4,'Python':'nohtyp12','stan':nats8,'apple':10}
i=0
out={}
while i<len(a):
    if type(a[i])==str:
        if(i%2==0):
            out[a[i]]=a[i][::-1]+str(len(a[i])*2)
        else:
            out[a[i]]=len(a[i])*2
    i+=1
print(out) 