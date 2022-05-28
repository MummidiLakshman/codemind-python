n=int(input())
a=list(map(int,input().split()))
b=int(input())
s=0
for i in range(0,b+1):
    s+=i
print(s)