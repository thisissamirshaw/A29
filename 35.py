#WAP to print last character of a list
# and it should be string and palindrome in nature 
# and its length should be more than 4.
lt = ['1','5','ram','Mango','Papaya','madam']
if type(lt[-1])== str:
    if lt[-1] == lt[::-1]:
      if len(lt[-1]) > 4:
         print(lt[-1])
      else:
        print("length is not more than 4 ")
    else:
       print("not a palindrome")    
else:
    print("not a string")