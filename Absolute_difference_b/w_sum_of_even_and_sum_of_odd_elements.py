n=int(input())
s=0
d=0
a=list(map(int,input().split()))
for i in range(0,n):
    if(a[i]%2==0):
        s+=a[i]
    else:
        d+=a[i]
ans=abs(s-d)
print(ans)