# 1、python之定义类并创建实例
在Python中，类通过 class 关键字定义。以 Person 为例，定义一个Person类如下：

```
class Person(object):
    pass
```
按照 Python 的编程习惯，类名以大写字母开头，紧接着是(object)，表示该类是从哪个类继承下来的。类的继承将在后面的章节讲解，现在我们只需要简单地从object类继承。

有了Person类的定义，就可以创建出具体的实例。创建实例使用 类名+`()`，类似函数调用的形式创建：
```
Bob = Person()
Jeff = Person()
```

# 2、python中创建实例属性
由于Python是动态语言，对每一个实例，都可以直接给他们的属性赋值。

```
Bob.sex = 'male'
Jeff.sex = 'female'
```

# 3、python中初始化实例属性
在定义 Person 类时，可以为Person类添加一个特殊的`__init__()`方法，当创建实例时，`__init__()`方法被自动调用，我们就能在此为每个实例都统一加上以下属性：

```
class Person(object):
    def __init__(self, name, gender, birth):
        self.name = name
        self.gender = gender
        self.birth = birth
```

`__init__()`方法的第一个参数必须是 `self`（也可以用别的名字，但建议使用习惯用法），后续参数则可以自由指定，和定义函数没有任何区别。

相应地，创建实例时，就必须要提供除 self 以外的参数：

```
xiaoming = Person('Xiao Ming', 'Male', '1991-1-1')
xiaohong = Person('Xiao Hong', 'Female', '1992-2-2')
```

有了`__init__()`方法，每个Person实例在创建时，都会有 name、gender 和 birth 这3个属性，并且，被赋予不同的属性值，访问属性使用`.`操作符。

注意，实例属性若以双下划线`__`开头，则被视为私有属性，不允许外部访问。

# 4、python中创建类属性
绑定在一个实例上的属性不会影响其他实例，但是，类本身也是一个对象，如果在类上绑定一个属性，则所有实例都可以访问类的属性，并且，所有实例访问的类属性都是同一个！也就是说，实例属性每个实例各自拥有，互相独立，而类属性有且只有一份。

定义类属性可以直接在 class 中定义：

```
class Person(object):
    address = 'Earth'
    def __init__(self, name):
        self.name = name
```

当实例属性和类属性重名时，实例属性优先级高，它将屏蔽掉对类属性的访问。

# 5、python中定义实例方法
一个实例的私有属性就是以__开头的属性，无法被外部访问，那这些属性定义有什么用？

虽然私有属性无法从外部访问，但是，从类的内部是可以访问的。除了可以定义实例的属性外，还可以定义实例的方法。

实例的方法就是在类中定义的函数，它的第一个参数永远是 `self`，指向调用该方法的实例本身，其他参数和一个普通函数是完全一样的：

```
class Person(object):
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name
```

`get_name(self)` 就是一个实例方法，它的第一个参数是self。`__init__(self, name)`其实也可看做是一个特殊的实例方法。

调用实例方法必须在实例上调用：
```
p1 = Person('Bob')
print p1.get_name()  # self不需要显式传入
# => Bob
```
在实例方法内部，可以访问所有实例属性，这样，如果外部需要访问私有属性，可以通过方法调用获得，这种数据封装的形式除了能保护内部数据一致性外，还可以简化外部调用的难度。

# 6、python中定义类方法
在class中定义的全部是实例方法，实例方法第一个参数 self 是实例本身。

要在class中定义类方法，需要这么写：

```
class Person(object):
    count = 0
    @classmethod
    def how_many(cls):
        return cls.count
    def __init__(self, name):
        self.name = name
        Person.count = Person.count + 1

print Person.how_many()
p1 = Person('Bob')
print Person.how_many()
```

通过标记一个 @classmethod，该方法将绑定到 Person 类上，而非类的实例。类方法的第一个参数将传入类本身，通常将参数名命名为 cls，上面的 cls.count 实际上相当于 Person.count。

因为是在类上调用，而非实例上调用，因此类方法无法获得任何实例变量，只能获得类的引用。


















