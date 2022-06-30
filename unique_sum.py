a=int(input())
b=list(map(int,input().split()))
s=[]
c=0
for i in b:
    if i not in s:
        s.append(i)
for i in s:
    c+=i
print(c)