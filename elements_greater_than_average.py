n=int(input())
a=list(map(int,input().split()))
s=sum(a)//n
c=0
for i in a:
    if(i>=s):
        c+=1
print(c)