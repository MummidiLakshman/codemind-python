a,b=map(int,input().split())
p=list(map(int,input().split()))
s=list(map(int,input().split()))
t=[]
y=[]
c=0
for i in p:
    if i not in t:
        t.append(i)
for j in s:
    if j not in y:
        y.append(j)
for i in t:
    for j in y:
        if(i==j):
            print(i,end=' ')