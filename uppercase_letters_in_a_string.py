n=str(input())
c=0
for i in range(len(n)):
    if(n[i]>='A' and n[i]<='Z'):
        c+=1
print(c)