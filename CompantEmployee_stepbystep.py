# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 16:05:07 2021

@author: xiaoh
"""
class Employee:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def fullname(self):
    print(self.firstname, self.lastname)

#Use the Employee class to create an object, and then execute the fullname method:

O = Employee("Kevin", "Long")
O.fullname()


"""Create a child class"""
class Company(Employee):
    
  pass  #Use the pass keyword when you do not want to add any other properties or methods to the class.
""" Use the Student class to create an object, and then execute the printname method:  """ 
O = Company("Kevin","Long")
O.fullname()

"""Add the __init__() Function"""
class Company(Employee):
  def __init__(self, fname, lname):
    Employee.__init__(self, fname, lname)
    #When you add the __init__() function, the child class will no longer inherit the parent's __init__() function
    #The child's __init__() function overrides the inheritance of the parent's __init__() function.
    
"""Use the super() Function"""
class Company(Employee):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)  #super() function will make the child class inherit all the methods and properties from its parent.
"""Add Properties"""
class Company(Employee):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.year_employed = 2020 #Add a property called year_employed to the Company class
    
"""Add a year parameter, and pass the correct year when creating objects"""
class Company(Employee):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.year_employed = year

O = Company("Kevin", "Long", 2020)

"""Add method"""
class Company(Employee):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.year_employedr = year

  def greeting(self): #Add a method called greeting to the Company class:
    print("Welcome", self.firstname, self.lastname, "to the class of", self.year_employed)
    

