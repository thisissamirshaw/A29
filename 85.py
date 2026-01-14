#WAP 
a=['Hello',5,9.8,[1,2],3+5j]
op=[5,1,1,2,1]
b=(int,complex,bool,float) #SVDT
out=[]
for i in a:
    if(type(i) in b):
        out+=[1]
    else:
        out+=[len(i)]
print(out)        
