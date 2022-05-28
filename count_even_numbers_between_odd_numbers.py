a=int(input())
c=0
b=list(map(int,input().split()))
for i in range(1,a-1):
    if(b[i]%2==0 and b[i-1]%2!=0 and b[i+1]%2!=0):
        c+=1
print(c)