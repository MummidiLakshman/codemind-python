a=int(input())
b=list(map(int,input().split()))
k=[]
f=0
for i in b:
    if i not in k:
        k.append(i)
for i in k:
    f+=i
print(f)