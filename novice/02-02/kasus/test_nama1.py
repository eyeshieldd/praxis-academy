import unittest

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age) 

class Mytest(unittest.TestCase):
    def test(self):
        self.assertEqual(p1.name, 'john' )
if __name__ == '__main__':
    unittest.main()