# 1、if，else-if, if-elif-else语句
注意`4空格缩进`和表达式后面的`冒号`

if语句
```
score = 75
if score >= 60:
  print 'passed'
```

else-if语句
```
score = 55
if score >= 60:
    print 'passed'
else:
    print 'failed'
```

if-elif-else语句
```
score = 85

if score >= 90:
    print 'excellent'
elif score >= 80:
    print 'good'
elif score >= 60:
    print 'passed'
else:
    print 'failed'
```

# 2、for循环
只有`for...in`循环，注意表达式后面的冒号

```
L = [75, 92, 59, 68]
sum = 0.0
for score in L:
    sum += score
print sum / 4
```
