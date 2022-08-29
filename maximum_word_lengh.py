n=input()
n=n.split()
s=[]
for i in n:
    c=len(str(i))
    s.append(c)
d=max(s)
print(d)
        