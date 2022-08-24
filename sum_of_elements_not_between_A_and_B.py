n=int(input())
a=list(map(int,input().split()))
b,c=map(int,input().split())
s=[]
d=[]
g=0
for i in range(b,c+1):
    s.append(i)
for i in a:
    if i not in s:
        d.append(i)
for i in d:
    g+=i
print(g)
    
