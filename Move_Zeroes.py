n=int(input())
a=list(map(int,input().split()))
h=[]
k=[]
for i in a:
    if i==0:
        h.append(i)
    else:
        k.append(i)
for i in h:
    k.append(i)
print(*k)
    
    