n=input()
n=n.split()
for i in n:
    s=min(i)
    break
for i in n[::-1]:
    d=max(i)
    break
print(s,d,end=' ')