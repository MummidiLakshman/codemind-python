n=int(input())
a=list(map(int,input().split()))
r=0
s=''
for i in a:
        s+=str(i)
d=int(s)
d=d+1
k=[]
while(d!=0):
    p=d%10
    k.append(p)
    d=d//10
o=len(k)
for i in range(o-1,-1,-1):
    print(k[i],end=' ')