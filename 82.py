#WAP to ext all the int from a given list using isinstance().
lt=[123,458,'op','liy']
out=[]
for i in lt:
    if(isinstance(i,int)):
        out+=[i]
print(out)


# # for i in range(len(lt)):
# #     if(type(lt[i])==int):
# #         out+=lt[i]
# print(out)    if isinstance(i,int):
    