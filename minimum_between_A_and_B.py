n=int(input())
a=list(map(int,input().split()))
c,d=map(int,input().split())
s=[]
v=0
for i in a:
    if i in range(c,d+1):
        s.append(i)
        v+=1
if(v==0):
    print('-1')
else:
    print(min(s))