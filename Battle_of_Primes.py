def prime(a):
    if(a==1):
        return 0
    for i in range(2,int(a**0.5)+1):
        if(a%i==0):
            return 0
    else:
        return 1
n=int(input())
s=int(input())
c=n+s
for i in range(1,100):
    if(prime(c+i)):
        print(i)
        break
