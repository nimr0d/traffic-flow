import numpy as np
import random

class traffic:
    def __init__(self, n=100,max_v=5,density=0.5,slow_down_random_probability=0.1,generate_car=2):
        self.n=n
        self.cars={}
        self.nextcars={}
        self.max_v=max_v
        self.density=density
        self.slow_down_random_probability=slow_down_random_probability
        all_generate_car={1:self.generate_car1,2:self.generate_car2}
        all_generate_car[generate_car]()
        self.printroad()


    def generate_car2(self):
        allcar=range(self.n)
        random.shuffle(allcar)
        for i in allcar[:int(self.n*self.density)]:
            self.cars[i]=random.randint(0,self.max_v)
        self.current_car_position=sorted(self.cars.keys())

    def generate_car1(self):
        for i in range(self.n):
            print(self.n,(self.n*self.density))
            if(i%(self.n/(self.n*self.density))==0):
                self.cars[i]=random.randint(0,self.max_v)
        self.current_car_position=sorted(self.cars.keys())

    # def generate_car(self):
    #     for i in range(self.n):
    #         if(random.random()<self.density):
    #             self.cars[i]=random.randint(0,self.max_v)
    #     self.current_car_position=sorted(self.cars.keys())

    def iteration(self):
        for i in self.current_car_position[::-1]:
            self.acceleration(i)
        for i in self.current_car_position[::-1]:
            self.slowing_down(i)
        for i in self.current_car_position[::-1]:
            self.randomization(i)
        copyofroad=self.getroad()
        for i in self.current_car_position[::-1]:
            self.car_motion(i)
        self.cars=self.nextcars
        self.nextcars={}
        self.current_car_position=sorted(self.cars.keys())

        return copyofroad


    def count_car(self):
        return(len(self.cars))

    def flow(self):
        num_site_pass=sum([self.cars[i] for i in self.cars])
        if num_site_pass==0:
            return 0
        else:
            return num_site_pass/float(self.n)


    def acceleration(self,car):
        if(self.cars[car]<self.max_v):
            self.cars[car]+=1

    def slowing_down(self,car):
        index=self.current_car_position.index(car)
        current=self.current_car_position[index%len(self.current_car_position)]
        before=self.current_car_position[(index+1)%len(self.current_car_position)]
        if((before-current)%self.n<=self.cars[current] and before!=current):
            self.cars[current]=(before-current)%self.n-1

    def randomization(self,car):
        if(random.random()<self.slow_down_random_probability):
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

    def getroad(self):
        board=['~' for i in range(self.n)]
        for i in self.cars:
            board[i]=int(self.cars[i])
        string=''
        for i in board:
            string+=str(i)
        return(string)
