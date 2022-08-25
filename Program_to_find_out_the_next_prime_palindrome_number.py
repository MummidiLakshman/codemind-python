def prime(n):
    if(n==1):
        return 0
    for i in range(2,int(n**0.5)+1):
        if(n%i==0):
            return 0
    return 1
def pal(n):
    s=n
    r=0
    while(n!=0):
        a=n%10
        r=r*10+a
        n=n//10
    if(s==r):
        return r
    else:
        return 0
n=int(input())
for i in range(n+1,n+10000):
    if(pal(i)):
        if(prime(i)):
            print(i)
            break