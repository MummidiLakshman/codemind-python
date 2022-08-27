n=input()
c=0
for i in n:
    if(ord(i)>=65 and ord(i)<=90):
        continue
    elif(ord(i)>=97 and ord(i)<=122):
        continue
    elif(ord(i)>=48 and ord(i)<=57):
        continue
    elif(i==' '):
        continue
    else:
        c+=1
print(c)
        