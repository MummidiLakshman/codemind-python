n=int(input())
b=[n]
b=list(map(int,input().split()))
d=0
for i in range(0,n):
    if(b[i]%2!=0):
        d=d+1
if(d<=2):
    print('YES')
else:
    print('NO')