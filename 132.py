def gen():
    print('Hello')
    yield 1
    print('Hiee')
    yield 2
    print('Bye')
    yield 3

print(tuple(gen()))

#yield is used to get array output or MVDT outputs 
#yield gives us the privilidge of solving sorting algos of mvdt
# and give output without using the print keyword
