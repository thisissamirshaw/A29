#WAP to input a str print a str with uppercase at even index of the input str,
#  without using any inbuilt library function upper() or lower() and dont use ord()
a=input("enter a string")
out=''
for i in a:
    if 'A'<=i<='Z':  #checking for uppercase
        if a.index(i)%2==0:
            out+=i
print(out)
    




# for i in a:
#     if a.index(i)%2==0:
#         out+=chr(ord(i)-32)  #upper case conversion without using inbuilt function
#     else:
#         out+=chr(ord(i)+32)  #lower case conversion without using inbuilt function
# print(out)




# a=input("enter a string")
# out=''
# for i in a:
#     if a.index(i)%2==0:
#         out+=i.upper()
#     else:
#         out+=i.lower()
# print(out)




# a=input("enter a string")
# out=''
# for i in a:
#     if a.index(i)%2==0:
#         out+=i.upper()
#     else:
#         out+=i.lower()
# print(out)