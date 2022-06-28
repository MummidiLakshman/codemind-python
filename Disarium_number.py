n=int(input())
g=n
d=len(str(n))
h=0
while(n!=0):
    s=n%10
    n=n//10
    f=pow(s,d)
    h+=f
    d-=1
if(g==h):
    print('True')
else:
    print('False')
        