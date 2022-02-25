# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 00:19:27 2021

@author: xiaohong Li
Polymorphism in python defines methods in the child class that have the 
same name as the methods in the parent class. In inheritance, the child class inherits
the methods from the parent class. Also, it is possible to modify a method in a child 
class that it has inherited from the parent class.

This is mostly used in cases where the method inherited from the parent class doesn’t
 fit the child class. This process of re-implementing a method in the child class is
 known as Method Overriding. Here is an example that shows polymorphism with inheritance:
     
"""

class Bird:
     def intro(self):
       print("There are different types of birds")
 
     def flight(self):
       print("Most of the birds can fly but some cannot")
 
class parrot(Bird):
     def flight(self):
       print("Parrots can fly")
 
class penguin(Bird):
     def flight(self):
       print("Penguins do not fly")
 
obj_bird = Bird()
obj_parr = parrot()
obj_peng = penguin()
 
obj_bird.intro()
obj_bird.flight()
 
obj_parr.intro()
obj_parr.flight()
 
obj_peng.intro()
obj_peng.flight()