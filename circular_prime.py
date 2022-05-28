def prime(a):
    if(a==1):
        return 0
    for i in range(2,int(a**0.5)+1):
        if(a%i==0):
            return 0
    return 1
a=int(input())
d=0
if(prime(a)):
    while(a>0):
        s=a%10
        d=d*10+s
        a=a//10
    if(prime(d)):
        print('circular prime')
    else:
        print('prime but not a circular prime')
else:
    print('not prime')