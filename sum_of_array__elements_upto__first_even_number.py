a=int(input())
b=list(map(int,input().split()))
f=0
for i in b:
    if i%2==0:
        break
    else:
        f+=i
print(f)