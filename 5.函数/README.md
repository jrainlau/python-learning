# 1、编写函数
在Python中，定义一个函数要使用 def 语句，依次写出函数名、括号、括号中的参数和冒号:，然后，在缩进块中编写函数体，函数的返回值用 return 语句返回。

我们以自定义一个求绝对值的 my_abs 函数为例：

```
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x
```

请注意，函数体内部的语句在执行时，一旦执行到return时，函数就执行完毕，并将结果返回。因此，函数内部通过条件判断和循环可以实现非常复杂的逻辑。

如果没有return语句，函数执行完毕后也会返回结果，只是结果为 None。

return None可以简写为return。

# 2、返回多值
类比于js的

```
{ x, y } = someFun()
```

python函数返回多值其实是返回一个tuple，不过可以省略括号

```
import math
def move(x, y, step, angle):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

x, y = move(100, 100, 60, math.pi / 6)
print x, y
```

# 3、默认参数
等价于js默认参数的写法
```
def func(x = 'hello'):
  return x
```

# 4、定义可变参数
类比于js的
```
function someFun(...args) {}
```

在python中，如果想让一个函数能接受任意个参数，我们就可以定义一个可变参数：

```
def fn(*args):
    print args
```
Python解释器会把传入的一组参数组装成一个tuple传递给可变参数，因此，在函数内部，直接把变量 args 看成一个 tuple 就好了。