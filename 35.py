#WAP to print last character of a list
# and it should be string and palindrome in nature 
# and its length should be more than 4.
list = ['1','5','ram','Mango','Papaya','madam']
if type(list[-1])== str:
    if list[-1] == list[::1]:
      if len(list[-1]) > 4:
         print(list[-1])
      else:
        print("length is not more than 4 ")
    else:
       print("not a palindrome")    
else:
    print("not a string")