L = list(range(1, 101))

print(L[:3])

print(L[-3:])

def trim(str = ''):
  if len(str) == 0:
    return ''
  if str[0] == ' ':
    str = str[1: ]
  if str[-1] == ' ':
    str = str[: -1]
  return str

print(trim(' Hello World '))
