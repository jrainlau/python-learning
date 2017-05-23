# 1、dict
类比js的`对象`

```
d = {
    'Adam': 95,
    'Lisa': 85,
    'Bart': 59,
    'Paul': 75
}

print len(d)
```

可以通过`len()`方法获取dict的大小

# 2、访问dict
通过`d[key]`或者`d.get(key)`来访问。区别是报错与返回`None`

# 3、赋值
直接赋值就行`d[key] = value`，若`key`存在，则新值覆盖旧值

# 4、使用`for...in`遍历dict
```
d = {
    'Adam': 95,
    'Lisa': 85,
    'Bart': 59
}
for key in d:
    print key, ':', d[key]
```

# 5、set
无序的不重复的List，等价于js的`set`
```
s = set(['Adam', 'Lisa', 'Bart', 'Paul', 'Paul'])

print s
```

set的内部元素必须是**不可变的**，所以不能嵌套list，只能嵌套tuple

因为无序，所以无法通过索引访问，只能通过`value in set`的`in`操作符判断元素是否在set内，也可以使用`for...in`循环进行遍历

# 6、操作set
使用`.add()`和`.remove()`方法进行添加或删除。注意使用`.remove()`时，如果元素不存在会报错，所以在使用前最好先判断元素是否在set内
```
s = set(['Adam', 'Lisa', 'Paul'])
if 'Adam' in s:
    s.remove('Adam')
else:
    s.add(name)
print s
```

