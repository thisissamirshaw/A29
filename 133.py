# WAP to op = {8:['Language','kkkkkkkk']}
a='Python is a language kkkkkkkk'.split()
out={}
max=0
for i in a:
    if max<=len(i):
        max=len(i)
out[max]=[] #crucial this 
for i in a:
    if len(i)==max:
        out[max]+=[i]  #this step is crucial
print(out) 


# ot=[89]
# print(ot)
# ot[1]=[8]
# print(ot)