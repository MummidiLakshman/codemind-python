a,b=map(int,input().split())
c=list(map(int,input().split()))
d=list(map(int,input().split()))
k=[]
for i in c:
    if i not in d:
        k.append(i)
for j in d:
    if j not in c:
        k.append(j)
for i in k:
    print(i,end=' ')
