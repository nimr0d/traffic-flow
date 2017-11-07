import numpy as np
import random

class Car: 
  def __init__(self, position = 0, velocity = 0, prev = None, next = None): 
    self.p = position
    self.v = velocity
    self.prev = prev    
    self.next = next
  def __str__(self): 
    return str(position) + ", " + str(velocity)

class traffic:
  def __init__(self, n = 100, max_v = 5, density = 0.03):
    self.n = n
    self.head = None
    self.max_v = max_v
    self.density = density
    #self.generate_cars()
    self.print_road()

  def iteration(self):
    

  def generate_cars(self):
    for i in range(self.n):
      if(random.random() < self.density):

  def print_road(self):

