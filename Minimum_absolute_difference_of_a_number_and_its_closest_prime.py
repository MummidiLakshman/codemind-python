def prime(n):
    if(n==1):
        return 0
    for i in range(2,int(n**0.5)+1):
        if(n%i==0):
            return 0
    return 1
n=int(input())
for i in range(n,0,-1):
    if(prime(i)):
        s=i
        break
for j in range(n,n+1000):
    if(prime(j)):
        d=j
        break
f=abs(n-s)
g=abs(n-d)
if(f<g):
    print(f)
else:
    print(g)