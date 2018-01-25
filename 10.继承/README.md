# 1、python中继承一个类
如果已经定义了Person类，需要定义新的Student和Teacher类时，可以直接从Person类继承：

```
class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
```
定义Student类时，只需要把额外的属性加上，例如score：

```
class Student(Person):
    def __init__(self, name, gender, score):
        super(Student, self).__init__(name, gender)
        self.score = score
```
一定要用 `super(Student, self).__init__(name, gender)` 去初始化父类，否则，继承自 Person 的 Student 将没有 name 和 gender。

函数`super(Student, self)`将返回当前类继承的父类，即 Person ，然后调用`__init__()`方法，注意self参数已在super()中传入，在`__init__()`中将隐式传递，不需要写出（也不能写）。

# 2、python中多重继承
除了从一个父类继承外，Python允许从多个父类继承，称为多重继承。

多重继承的继承链就不是一棵树了，它像这样：

```
class A(object):
    def __init__(self, a):
        print 'init A...'
        self.a = a

class B(A):
    def __init__(self, a):
        super(B, self).__init__(a)
        print 'init B...'

class C(A):
    def __init__(self, a):
        super(C, self).__init__(a)
        print 'init C...'

class D(B, C):
    def __init__(self, a):
        super(D, self).__init__(a)
        print 'init D...'
```

像这样，D 同时继承自 B 和 C，也就是 D 拥有了 A、B、C 的全部功能。多重继承通过 super()调用__init__()方法时，A 虽然被继承了两次，但__init__()只调用一次：

```
d = D('d')
init A...
init C...
init B...
init D...
```

多重继承的目的是从两种继承树中分别选择并继承出子类，以便组合功能使用。