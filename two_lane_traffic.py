import numpy as np
import random

class Car: 
  def __init__(self, position = 0, lane = 0, velocity = 0, aggressiveness = 0, id = 0): 
    self.p = position
    self.l = lane
    self.v = velocity
    self.a = aggressiveness
    self.id = id

class Traffic:
  def __init__(self, n = 100, max_v = 5, density = .1, prob = 0.1):
    self.n = n
    self.max_v = max_v
    self.density = density
    self.prob = prob
    self.num_cars = 0
    self.road = [[self.new_car(pos, lane) for pos in range(n)] for lane in range(2)]
    self.flow = self.max_v * self.num_cars
  def new_car(self, pos, lane):
    if random.random() > self.density:
      return None
    self.num_cars += 1
    return Car(pos, lane, self.max_v, id = self.num_cars - 1)
  def next_car_dist(self, p, arr, nonev = None):
    for x in range(0, self.max_v + 1):
      pos = (p + x) % self.n
      if arr[pos] != nonev:
        return x
    return self.max_v + 1
  def prev_car_dist(self, p, arr, nonev = None):
    for x in range(0, self.max_v + 1):
      pos = (p - x) % self.n
      if arr[pos] != nonev:
        return x
    return self.max_v + 1
  def iterate(self):
    rh = [np.zeros(self.n, dtype = bool), np.zeros(self.n, dtype = bool)]
    for l in range(2): # Mark switching cars
      lanes = [self.road[l], self.road[1 - l]]
      for p in range(self.n):
        car = lanes[0][p]    
        if car != None:
          d0 = self.next_car_dist(car.p + 1, lanes[0]) + 1
          d1 = self.next_car_dist(car.p, lanes[1])
          p1 = self.prev_car_dist(car.p, lanes[1])
          rh[l][car.p] = True
          if d1 > d0 and p1 >= self.max_v / 2: # Switch condition
            car.l = 1 - l
            rh[1 - l][car.p] = True
    for l in range(2): # Update velocities and positions
          lane = self.road[l]
          for p in range(self.n):
            car = lane[p]    
            if rh[l][p] and car != None:
              self.flow -= car.v
              d = self.next_car_dist(car.p + 1, rh[l], False) + 1
              if d > car.v + 1 and car.v < self.max_v:
                car.v += 1
              elif d <= car.v:
                car.v = d - 1
              if car.v > 0 and random.random() < self.prob:
                car.v -= 1
              lane[car.p] = None
              car.p = (car.p + car.v) % self.n
              self.road[car.l][car.p] = car
              self.flow += car.v


  def __str__(self):
    ret = ""
    for p in range(self.n):
      ret += "_" if self.road[0][p] == None else u"\u25A0"
    ret += "\n"
    for p in range(self.n):
      ret += "_" if self.road[1][p] == None else u"\u25A0"
    ret += "\n"
    return ret