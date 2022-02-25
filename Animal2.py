# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 00:12:45 2021

@author: xiaohong Li

We will be defining functions in the derived class that has the same name as 
the functions in the base class. Here, we re-implement the functions in the derived class. 
The phenomenon of re-implementing a function in the derived class is known as Method Overriding.

Polymorphism with Inheritance
"""

class Animal: 
  def type(self): 
    print("Various types of animals") 
       
  def age(self): 
    print("Age of the animal.") 
     
class Rabbit(Animal): 
  def age(self): 
    print("Age of rabbit.") 
       
class Horse(Animal): 
  def age(self): 
    print("Age of horse.") 
       
obj_animal = Animal() 
obj_rabbit = Rabbit() 
obj_horse = Horse() 
   
obj_animal.type() 
obj_animal.age() 
   
obj_rabbit.type() 
obj_rabbit.age() 
   
obj_horse.type() 
obj_horse.age() 