n=int(input())
a=list(map(int,input().split()))
k=int(input())
g=[]
h=0
for i in a:
    if a.count(i)==k:
        h=1
        g.append(i)
d=set(g)
f=list(d)
for i in f:
    print(i,end=' ')
if(h==0):
    print('-1')
        
        