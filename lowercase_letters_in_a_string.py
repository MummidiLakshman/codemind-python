n=str(input())
c=0
for i in range(len(n)):
    if(n[i]>='a' and n[i]<='z'):
        c+=1
print(c)