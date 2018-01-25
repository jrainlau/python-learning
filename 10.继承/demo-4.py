class Animal(object):
  def eat(self):
    print('Eatting...')

class Bird(Animal):
  def fly(self):
    print('Flying')

class Mammal(Animal):
  def born(self):
    print('Drink milk')

class Pet(Animal):
  def cute(self):
    print('Very cute')

class Dog(Mammal, Pet):
  pass

dog = Dog()
dog.eat()
dog.cute()
dog.born()