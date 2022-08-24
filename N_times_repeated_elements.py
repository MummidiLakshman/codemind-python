n=int(input())
a=list(map(int,input().split()))
b=int(input())
s=[]
d=[]
c=0
for i in a:
    if a.count(i)==b:
        s.append(i)
        c+=1
for i in s:
    if i not in d:
        d.append(i)
if(c==0):
    print('-1')
else:
    print(*d)