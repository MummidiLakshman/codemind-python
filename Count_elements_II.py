a,b=map(int,input().split())
c=list(map(int,input().split()))
d=list(map(int,input().split()))
f=[]
g=[]
h=0
p=0
for i in c:
    if i not in f:
        f.append(i)
for i in d:
    if i not in g:
        g.append(i)
for i in f:
    if i not in g:
        h+=1
for i in g:
    if i not in f:
        p+=1
s=h+p
print(s)