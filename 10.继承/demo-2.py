# 使用__slots__

class Student(object):
    __slots__ = ('score', 'name', 'age')
    def set_score(self, score):
        self.score = score
    def get_score(self):
        return self.score

bob = Student()
bob.set_score(100)
print(bob.get_score())

bob.name = 'Bob'
bob.xxx = 'xxx'
