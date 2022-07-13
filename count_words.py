n=input()
n=n.lower()
s=n.split()
v='aeiou'
c='bcdfghjklmnpqrstvwxyz'
h=0
f=0
for i in s:
    for j in i:
        k=j
        break
    for j in i[::-1]:
        g=j
        break
    if k in v :
        if g in c:
            h+=1
print(h)