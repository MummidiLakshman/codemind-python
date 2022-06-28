n=int(input())
s=n*n
r=0
k=0
while(n!=0):
    f=n%10
    r=r*10+f
    n=n//10
y=r*r
while(y!=0):
    p=y%10
    k=k*10+p
    y=y//10
if(s==k):
    print('True')
else:
    print('False')
    