n=int(input())
a=list(map(int,input().split()))
k,p=map(int,input().split())
s=0
c=0
for i in a:
    if i in range(k,p+1):
        s+=i
print(s)
        
    