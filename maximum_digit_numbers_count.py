n=int(input())
a=list(map(int,input().split()))
d=[]
for i in a:
    s=len(str(i))
    d.append(s)
f=max(d)
for i in a:
    if(len(str(i))==f):
        print(i,end=' ')