n=input()
n=n.split()
v='aeiouAEIOU'
c=0
for i in n:
    if (i[0]) in v and i[-1] not in v:
        c+=1
print(c)