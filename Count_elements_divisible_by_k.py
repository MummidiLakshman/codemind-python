n,m=map(int,input().split())
c=0
a=list(map(int,input().split()))
for i in range(0,n):
    if(a[i]%m==0):
        c+=1
print(c)
