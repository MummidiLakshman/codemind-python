n=int(input())
a=list(map(int,input().split()))
k,p=map(int,input().split())
s=[]
c=0
for i in a:
    if i  not in range(k,p+1):
        s.append(i)
        c=1
if(c==1):
    print(min(s))
else:
    print('-1')
        
    