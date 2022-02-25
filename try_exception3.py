# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 01:36:37 2021

@author: xiaoh
"""

try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")
