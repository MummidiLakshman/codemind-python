a=str(input())
s=0
for i in range(0,len(a)):
    if(a[i]>='0' and a[i]<='9'):
        s=s+int(a[i])
print(s)