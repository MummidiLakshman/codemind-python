n=input()
p=input()
for i in n:
    if p in n:
        s=n.index(p)
        print('True')
        print(s)
        break
else:
    print('False')