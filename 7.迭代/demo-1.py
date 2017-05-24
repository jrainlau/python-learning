L = ['Adam', 'Lisa', 'Bart', 'Paul']
for index, name in enumerate(L):
    print index + 1, '-', name



d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59, 'Paul': 74 }
sum = 0.0
for s in d.itervalues():
    sum += s
print 'average score:', sum / len(d)



d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59 }
for key, value in d.items():
    print key, ':', value