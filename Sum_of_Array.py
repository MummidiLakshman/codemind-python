n=int(input())
s=0
a=list(map(int,input().split()))
for i in range(0,n):
        s+=a[i]
print(s)