n=int(input())
s=0
b=0
t=n
while(n>0):
    s=n%10
    b=b*10+s
    n=n//10
if(t==b):
    print('True')
else:
    print('False')