a,b=map(int,input().split())
c=list(map(int,input().split()))
d=list(map(int,input().split()))
k=[]
s=[]
t=0
for i in c:
    if i not in k:
        k.append(i)
for j in d:
    if j not in s:
        s.append(j)
for i in k:
    for j in s:
        if(i==j):
            print(i,end=' ')