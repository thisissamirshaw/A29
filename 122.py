#WAP ext only integers from a list using recursion
def ext(lt,out=[],i=0):
    if i>=len(lt):
        return out
    if type(lt[i])==int:
        out.append(lt[i])
    return ext(lt,out,i+1)
print(ext([7,8,'liy',0]))    
