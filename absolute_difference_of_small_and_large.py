n=input()
n=n.split()
for i in n:
    s=ord(min(i))
    h=ord(max(i))
    d=abs(s-h)
    print(d,end=' ')