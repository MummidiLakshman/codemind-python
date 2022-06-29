a=int(input())
b=list(map(int,input().split()))
k,j=map(int,input().split())
s=0
for i in range(0,a):
    if(b[i]>=k and b[i]<=j):
        s+=b[i]
print(s)
