n=int(input())
s=list(map(int,input().split()))
a,b=map(int,input().split())
c=0
for i in s:
    if i not in range(a,b+1):
        c=1
        print(i,end=' ')
if(c==0):
    print('-1')