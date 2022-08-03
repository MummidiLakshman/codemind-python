a=int(input())
b=list(map(int,input().split()))
f=0
g=0
for i in range(0,a//2):
    f+=b[i]
for j in range(a//2,a):
    g+=b[j]
s=abs(f-g)
print(s)