a=input()
d=len(str(a))
s=''
for i in a:
    if i not in s:
        s+=i
    b=len(str(s))
    if(d==b):
          print('Unique Number')
          break
else:
    print('Not Unique Number')