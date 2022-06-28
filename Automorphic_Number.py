n=int(input())
d=len(str(n))
f=n*n
s=f%pow(10,d)
if(n==s):
    print('Automorphic Number')
else:
    print("Not an Automorphic Number")
    