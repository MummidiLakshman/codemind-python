n=int(input())
a=list(map(int,input().split()))
l=[]
c=0
s=[]
for i in a:
    if i not in s:
        s.append(i)
        print(i,a.count(i),end=' ')
    