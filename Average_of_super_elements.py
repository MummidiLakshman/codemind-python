n=int(input())
a=list(map(int,input().split()))
s=[]
f=0
for i in a:
    if a.count(i)==i:
        s.append(i)
        f+=1
if(f==0):
    print('-1')
else:
    b=set(s)
    l=len(b)
    d=sum(b)/l
    print("%.2f"%d)


        