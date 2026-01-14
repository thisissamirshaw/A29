#WAP to extract the integers from a given list
lt=eval(input("enter a list"))
i=0
out=[]
while i<len(lt):
    if type(lt[i])==int:
        out+=[lt[i]]
        #out.append(lt[i])
    i+=1    
print(out)        
