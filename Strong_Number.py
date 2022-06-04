def fact(n):
    v=1
    for i in range(1,n+1):
        v*=i
    return v
n=int(input())
b=0
g=n
while(n>0):
    s=n%10
    b+=fact(s)
    n=n//10
if(b==g):
    print('The number {0} is a strong number'.format(g))
else:
    print('The number {0} is not a strong number'.format(g))