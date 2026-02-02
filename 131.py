# wap to extract all the integers from a given list
def genx(a):
    for i in a :
        if type(i)==int:
            yield i
print(list(genx([10,35,"Hello",5.3,101])))


# wap to extract integer from list also they must be palindrome 
def genp(a):
    for i in a :
        if type(i)==int and str(i)==str(i)[::-1]:
            yield i
print(list(genp([123,121,"Hello",5.3,1221])))

#wap to take number whose ten multiple store in tuple

def ten_multiples(n):
    for i in range(1, 11):
        yield n * i

num = int(input("Enter a number: "))

mul_tuple = tuple(ten_multiples(num))

print("multiples stored in tuple:")
print(mul_tuple)


#input=[111, 12, "hello", 7777, 3.5]
#output=[(111, 3), (7777, 4)]

def gen_ex(a,op):
    for i in a:
        if type(i)==int and str(i)==str(i)[::-1]:
            yield (i,len(str(i)))            
print(list(gen_ex([111,12,"hello",7777,3.5],[])))


# store prime 1 to 1000 in list
def is_prime(num):
    for i in range(2,num):
        if num %i==0:
            return "Not Prime"
    return "Prime"
def prime():
    for i in range(1,1001):
        if is_prime(i)=="Prime":
            yield i
print(list(prime()))

# wap to check if number is perfect
def is_perfect(num):
    sum=0
    for i in range(1,num):
        if num%i==0:
            sum+=i
    if sum == num:
        return "perfect"
    else:
        return "not perfect"
def check():
    for i in range(1,1000):
        if is_perfect(i)=="perfect":
            yield i
            
print(list(check()))