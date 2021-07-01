#1
class MyClass:
  x = 5

#2
class MyClass:
  x = 5
p1 = MyClass()

#3
class MyClass:
  x = 5

p1 = MyClass()

print(p1.x)

#4
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age