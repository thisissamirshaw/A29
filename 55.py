#WAP to extract all the  str from a given list at even index position and their length should be atleast than 3 without using inbuilt function
lt=['eve','evve',]
i=0
out=[]
while i<len(lt):
    if(type(lt[i])==str and i%2==0 and len(lt[i])>=3):
        out.append(lt[i])
    i+=1
print(out)