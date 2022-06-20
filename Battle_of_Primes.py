def prime(a):
    if(a==1):
        return 0
    for i in range(2,(a//2)+1):
        if(a%i==0):
            return 0
    return 1
a=int(input())
b=int(input())
c=a+b
for i in range(1,100):
    if(prime(c+i)):
        print(i)
        break