s=7
g=int(input('guess the number:'))
while g!=s:
  if g<s:
    print('too low')
  else:
    print('too high')
  g=int(input('guess again:'))
print('you got it!')