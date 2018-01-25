L = ['Adam', 'Lisa', 'Bart', 'Paul']
for index, name in enumerate(L):
    print(index + 1, '-', name)



d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59, 'Paul': 74 }
sum = 0.0
for s in d.values():
    sum += s
print('average score:', sum / len(d))



d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59 }
for key, value in d.items():
    print(key, ':', value)


def findMinAndMax(list = []):
  if len(list) == 0:
    max = None
    min = None
  else:
    max = list[0]
    min = list[0]
  for item in list:
    if item > max:
      max = item
    if item < min:
      min = item
  return (min, max)

print(findMinAndMax([1, 2, 4, 5, -1, 3]))
