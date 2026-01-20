#WAP to find sum of numbers in your email id using function



def sumel():
    eml='mitchellsamir999@gmail.com'
    sum=0
    for i in eml:
        if '0'<=i<='9':
            sum+=int(i)
    print(sum)  
sumel()          
            