# WAP if a number is divisible by 3 print square of it 
# and if num is divisible by 5 print cube of it 
# and if divisible by both 3 and 5 
# print double of that number between 1 to 50.
i = 1
while i < 51:
    if i % 3==0 and i % 5 == 0:
        print(2*i)
    elif i % 3 == 0:
        print(i * i)
    elif i % 5 == 0:
        print(i ** 3) 
    i += 1    