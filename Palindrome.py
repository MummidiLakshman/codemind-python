n=int(input())
g=n
d=0
while(n!=0):
    s=n%10
    d=d*10+s
    n=n//10
if(g==d):
    print('True')
else:
    print('False')