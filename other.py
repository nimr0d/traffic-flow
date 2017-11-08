import numpy as np
import random

class traffic:
    def __init__(self, n=100,max_v=5,density=0.5,random_probability=0.1):
        self.n=n
        self.cars={}
        self.nextcars={}
        self.max_v=max_v
        self.density=density
        self.random_probability=random_probability
        self.generate_car()
        self.printroad()

    def generate_car(self):
        for i in range(self.n):
            if(random.random()<self.density):
                self.cars[i]=random.randint(0,self.max_v)
        self.current_car_position=sorted(self.cars.keys())

    def iteration(self):
        count_car=len(self.cars)
        for i in self.current_car_position[::-1]:
            self.acceleration(i)
        for i in self.current_car_position[::-1]:
            self.slowing_down(i)
        for i in self.current_car_position[::-1]:
            self.randomization(i)
        self.printroad()
        for i in self.current_car_position[::-1]:
            self.car_motion(i)
        self.cars=self.nextcars
        self.nextcars={}
        self.current_car_position=sorted(self.cars.keys())




    def acceleration(self,car):
        if(self.cars[car]<self.max_v):
            self.cars[car]+=1

    def slowing_down(self,car):
        index=self.current_car_position.index(car)
        current=self.current_car_position[index%len(self.current_car_position)]
        before=self.current_car_position[(index+1)%len(self.current_car_position)]
        if((before-current)%self.n<=self.cars[current]):
            self.cars[current]=(before-current)%self.n-1

    def randomization(self,car):
        if(random.random()<self.random_probability):
            if(not self.cars[car]==0):
                self.cars[car]-=1

    def car_motion(self,car):
        velocity=self.cars[car]
        nextposition=(velocity+car)%self.n
        self.nextcars[nextposition]=velocity

    def get_car(self):
        return self.cars

    def printroad(self):
        board=['~' for i in range(self.n)]
        for i in self.cars:
            board[i]=int(self.cars[i])
        string=''
        for i in board:
            string+=str(i)
        print(string)
