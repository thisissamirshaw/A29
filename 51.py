# #WAP to find number 341 from 143 without using indexing and typecasting.
# a = 143 
# result = ((a%10)*100+(a%100)//10*10+a//100)
# print(result)

# #---------------------------OR---------------------------------
a=int(input("enter no for rev "))
rev=0
while a!=0:
    id = a%10
    rev=rev*10+id
    a=a//10
print(rev)    
# #----------------------------OR-----------------------------------
# #Sum Until Threshold  
# # Write a program using a while loop that keeps asking the user to enter numbers. 
# # Stop when the total sum exceeds 100, and then print the sum and how many 
# # numbers were entered
# total=0
# count=0
# while total<=100:
#     num= int(input("Enter a number: "))
#     total+=num
#     count+=1
# print(total)
# print(count)  