n=int(input())
s=0
v=0
a=list(map(int,input().split()))
for i in range(0,n):
    s=s+a[i]
    d=s//n
for i in range(0,n):
    if(d>=a[i]):
        v+=1
print(v)