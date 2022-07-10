a=int(input())
b=list(map(int,input().split()))
k=[]
f=0
for i in b:
    if i not in k:
        k.append(i)
for i in range(0,len(k)):
    if(k[i]%2!=0):
        f+=1
print(f)