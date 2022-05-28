n=int(input())
a=list(map(int,input().split()))
s=0
d=0
for i in range(0,n//2):
    s+=a[i]
for i in range(n//2,n):
    d+=a[i]
ans=abs(s-d)
print(ans)