n=input()
n=n.split()
for i in n:
    k=min(i)
    break
s=n[::-1]
for i in s:
    h=max(i)
    break
print(k,h)
    