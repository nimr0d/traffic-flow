import numpy as np
import random
class traffic:
    def __init__(self, n=100,max_v=5,init_density=0.03):
        self.road=np.zeros(n)
        self.max_v=max_v
        self.init_density=init_density
        self.generate_car()
        self.printroad()

    def generate_car(self):
        for i in range(len(self.n)):
            if(random.random<self.init_density):
                self.road[i]=1

    # def iteration(self):



    def printroad(self):
        print(self.road)
