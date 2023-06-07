def lltod(ll):
  a = {}
  for i,e in enumerate(ll):
      a[e]=i
  return a
print(lltod(['casa','cotxe','cadira','taula']))

def ltod(l):
    return {value: key for value, key in enumerate(l)}

print(ltod(['casa','cotxe','cadira','taula']))
