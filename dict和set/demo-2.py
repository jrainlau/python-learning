s = set(['Adam', 'Lisa', 'Bart', 'Paul', 'Paul'])
print s

s = set([('Adam', 95), ('Lisa', 85), ('Bart', 59)])
for x in s:
    print x[0] + ':', x[1]

s = set(['Adam', 'Lisa', 'Paul'])
if 'Adam' in s:
    s.remove('Adam')
else:
    s.add('Adam')
print s