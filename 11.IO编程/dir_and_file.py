import os
print(os.path.abspath('.'))

os.path.join(os.path.abspath('.'), 'testdir')
os.mkdir(os.path.abspath('.') + '/testdir')

arr = [x for x in os.listdir('.') if os.path.isfile(x)]

print(arr)