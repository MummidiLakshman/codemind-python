n=int(input())
a=list(map(int,input().split()))
b,c=map(int,input().split())
s=[]
d=[]
r=[]
maxx=999999
h=0
for i in range(b,c+1):
    s.append(i)
for i in a:
    if i not in s:
        d.append(i)
for i in d:
    if i not in r:
        r.append(i)
for i in r:
    if(i<maxx):
        maxx=i
        h+=1
if(h==0):
    print("-1")
else:
    print(maxx)

    
