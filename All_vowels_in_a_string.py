n=input()
v='aeiou'
s=''
for i in n:
    if i in v:
        s+=i
#print(s)
for i in v:
    if i not in s:
        print('False')
        break
else:
    print('True')
#print(n)