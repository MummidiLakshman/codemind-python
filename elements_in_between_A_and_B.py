a=int(input())
b=list(map(int,input().split()))
s,t=map(int,input().split())
c=0
for i in range(0,a):
    if(b[i]>=s and b[i]<=t):
        c=1
        print(b[i],end=' ')
if(c==0):
    print('-1')