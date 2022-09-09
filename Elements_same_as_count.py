n=int(input())
a=list(map(int,input().split()))
l=[]
for i in a:
    if a.count(i)==i:
        l.append(i)
p=[]
for i in l:
    if i not in p:
        p.append(i)
if(len(p)==0):
    print("-1")
else:
    for i in p:
        print(i,end=' ')
    