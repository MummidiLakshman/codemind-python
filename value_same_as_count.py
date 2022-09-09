n=int(input())
a=list(map(int,input().split()))
l=[]
c=0
for i in a:
    if a.count(i)==i:
        l.append(i)
p=[]
for i in l:
    if i not in p:
        p.append(i)
        c+=1
print(c)
    