n=int(input())
a=list(map(int,input().split()))
k=[]
for i in a:
    s=len(str(i))
    k.append(s)
d=max(k)
for i in a:
    if(len(str(i))==d):
        print(i,end=' ')