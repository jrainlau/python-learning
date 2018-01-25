with open('./test.md', 'r') as f:
  print(f.read())

with open('./test.md', 'r') as f:
  print(f.read(5))

with open('./test.md', 'r') as f:
  print(f.readlines(1))

with open('./test.md', 'a') as f:
  f.write('\n\nWrite something...')