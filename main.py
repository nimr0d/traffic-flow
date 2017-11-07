import numpy as np
import random
class traffic:
    def __init__(self, n = 100, max_v = 5, density = 0.03):
        self.n = n
        self.road = np.zeros(n)
        self.max_v = max_v
        self.density = density
        self.generate_car()
        self.print_road()

    def generate_car(self):
        for i in range(self.n):
            if(random.random() < self.density):
                self.road[i] = 1

    # def iteration(self):



    def print_road(self):
        print(self.road)
