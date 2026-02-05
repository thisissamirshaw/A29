# WAJP to get digit sum of a number by using
# recursion.
def digit_sum(n):
    if n == 0 or n==1:
        return n
    else:
        return (n % 10) + digit_sum(n // 10)
print(digit_sum(int(input("enter any no: "))))