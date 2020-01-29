'''
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def Grade():
      print('I got an A in my Class')

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)
  

Student("Mike", "Olsen" , 2018).printname()
Student("Emmanuel", "Kobe" ,2018).welcome()



# Iterables and Iterators
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit)*3)

import mymodule

mymodule.greeting("Wale")
'''

price = 49

print("The price is {} dollars".format(price))
















  
