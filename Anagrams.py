n=input()
c=input()
n=n.lower()
c=c.lower()
for i in n:
    if i not in c:
        print('False')
        break
else:
    print('True')