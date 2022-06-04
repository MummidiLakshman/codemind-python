n=int(input())
d=len(str(n))
s=n*n
t=len(str(s))
h=s%pow(10,d)
if(h==n):
    print('Automorphic Number')
else:
    print('Not an Automorphic Number')