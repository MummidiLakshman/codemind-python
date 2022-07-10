a,b=map(int,input().split())
c=list(map(int,input().split()))
d=list(map(int,input().split()))
k=[]
p=[]
l=0
for i in c:
    if i not in k:
        k.append(i)
for j in d:
    if j not in p:
        p.append(j)
for i in k:
    for j in p:
        if(i==j):
            l+=1
print(l)