n=int(input())
a=list(map(int,input().split()))
m=0
c=0
for i in a:
    if a.count(i)==1:
        if(i>m):
            m=i
            c+=1
if(c==0):
    print('-1')
else:
    print(m)