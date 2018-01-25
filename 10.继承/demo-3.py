# 使用@property
# 把一个getter**方法**变成属性，只需要加上@property就可以了

class Student(object):
  @property
  def score(self):
    print('Getting score: ' + str(self.__score))
    return self.__score

  @score.setter
  def score(self, value):
    if not isinstance(value, int):
      raise ValueError('score must be an integer')
    if value < 0 or value > 100:
      raise ValueError('score must between 0 ~ 100!')
    print('Setting score: ' + str(value))
    self.__score = value


student = Student()
student.score = 88
student.score