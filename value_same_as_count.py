n=int(input())
a=list(map(int,input().split()))
c=0
s=[]
for i in range(0,n):
    if a.count(a[i])==a[i] and a[i] not in s:
        s.append(a[i])
        c+=1
print(c)