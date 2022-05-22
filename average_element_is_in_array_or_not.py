n=int(input())
s=0
a=list(map(int,input().split()))
for i in range(0,n):
    s=s+a[i]
d=s//n
if d in a:
    print('True')
else:
    print('False')