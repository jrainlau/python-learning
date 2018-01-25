# 避免默认参数累积
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L

print(add_end())
print(add_end())
print(add_end())

# 可变参数
def sum(*numbers):
  sum = 0
  for n in numbers:
    sum += n
  return sum

print(sum(1, 2, 3))

# 关键字参数
def person(name, age, **kw):
  print('name:', name, 'age:', age, 'other:', kw)

person('Jrain', '24', city = 'SZ')

extract = {
  'city': 'SZ',
  'height': '100',
  'weight': '200'
}

person('TZC', '24', **extract)

# 命名关键字参数
def person(name, age, *, city, job):
  print(name, age, city, job)

person('DBJ', '24', city = 'xx', job = 'yy')

# 参数组合
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

f1('A', 'B', 'C', 'DE', 'FG', xxx='123')
f2('A', 'B', 'CCC', d='DDD', eee='EEE')
