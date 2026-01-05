#wap to check number is single digit , double digit, three digit and four digit number.

num = int(input("Enter a number"))
if 0<=num<=9:
    print(num,"num is one digit number")
elif 10<= num <=99:
    print(num,"num is two digit number")
elif 100<= num <=999:
    print(num,"num is three digit number")
elif 1000<= num<=9999:
    print(num,"num is four digit number")
else:
    print(num,"is greater that 4 digit number")