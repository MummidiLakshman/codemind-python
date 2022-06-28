n=int(input())
m=int(input())
s=0
g=0
for i in range(1,n):
    if(n%i==0):
        s+=i
for i in range(1,m):
    if(m%i==0):
        g+=i
if(m==s):
    print('Amicable')
else:
    print('Not Amicable')