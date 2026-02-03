def gen():
    print('Hello')
    yield 1
    print('Hiee')
    yield 2
    print('Bye')
    yield 3

print(list(gen()))
