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

class Traffic:
  def __init__(self, n = 100, max_v = 5, density = 0.03, prob = 0.1):
    self.n = n
    self.head = None
    self.max_v = max_v
    self.density = density
    self.prob = prob
    
  def iterate(self):
    car = self.head
    while car != None:
      d = self.n - car.p + 1 if car.next == None else car.next.p - car.p
      if d > car.v + 1 and car.v < self.max_v:
        car.v += 1
      elif d <= car.v:
        car.v = d - 1
      if car.v > 0 and random.random() < self.prob:
        car.v -= 1
      car.p += car.v
      if car.p >= self.n:
        if car.prev == None:
          self.head = None
        else:
          car.prev.next = None
        car.prev = None
      car = car.next
    if self.head != None and self.head.p != 0 and random.random() < self.density:
      new_car = Car(0, self.max_v, next = self.head)
      self.head.prev = new_car
      self.head = new_car
    if self.head == None and random.random() < self.density:
      self.head = Car(0, self.max_v)
    
  def __str__(self):
    ret = ""
    car = self.head
    i = 0
    while car != None:
      while i < car.p:
        ret += " "
        i += 1
      ret += u"\u25A0"
      i += 1
      car = car.next
    return ret