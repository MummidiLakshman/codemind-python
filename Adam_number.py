n=int(input())
s=n*n
d=0
h=0
while(n>0):
    a=n%10
    d=d*10+a
    n=n//10
f=d*d
while(f>0):
    g=f%10
    h=h*10+g
    f=f//10
if(s==h):
    print('True')
else:
    print('False')