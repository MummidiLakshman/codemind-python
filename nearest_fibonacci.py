def fib(n):
    a=0
    b=1
    c=a+b
    while(c<n):
        c=a+b
        a=b
        b=c
    if(c==n):
        return 1
    else:
        return 0
n=int(input())
for i in range(n-1,0,-1):
    if(fib(i)):
        s=i
        break
for i in range(n+1,n+10000):
    if(fib(i)):
        d=i
        break
if(abs(n-s)<abs(n-d)):
    print(s)
elif(abs(n-s)==abs(n-d)):
    print(s,d,end=' ')
else:
    print(d)