class Person(object):
    def __init__(self, name, sex, bir, job):
        self.name = name
        self.sex = sex
        self.bir = bir
        self.job = job
        self.__private = 'secret'

xiaoming = Person('Xiao Ming', 'Male', '1990-1-1', 'Student')

print (xiaoming.name)
print (xiaoming.job)


class Person(object):
    count = 0
    def __init__(self, name):
        Person.count = Person.count + 1
        self.name = name
p1 = Person('Bob')
print (Person.count)

p2 = Person('Alice')
print (Person.count)

p3 = Person('Tim')
print (Person.count)