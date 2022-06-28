n=int(input())
f=0
p=1
while(n!=0):
    s=n%10
    f+=s
    p=p*s
    n=n//10
if(f==p):
    print('Spy Number')
else:
    print('Not Spy Number')