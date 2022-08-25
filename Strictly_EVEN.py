n=int(input())
a=list(map(int,input().split()))
f=0
c=0
for i in range(0,n):
    if(i%2==0 and a[i]%2==0):
        f+=1
    if(a[i]%2==0):
        c+=1
if(f==c):
    print('True')
else:
    print('False')
            