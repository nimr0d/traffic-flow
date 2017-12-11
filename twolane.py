import numpy as np
import random
import bisect

class traffic:
    def __init__(self, n=100,max_v=5,density=0.2,slow_down_random_probability=0.1,generate_car=1):
        self.n=n
        self.cars=[]
        self.cars.append({})
        self.cars.append({})
        self.nextcars={}
        self.max_v=max_v
        self.density=density
        self.slow_down_random_probability=slow_down_random_probability
        all_generate_car={1:self.generate_car1,2:self.generate_car2}
        all_generate_car[generate_car]()
        self.printroad()


    def generate_car2(self):
        allcar=range(self.n*2)
        random.shuffle(allcar)
        for i in allcar[:int(self.n*2*self.density)]:
            self.cars[i/100][i%100]=random.randint(0,self.max_v)
        self.current_car_position=[sorted([j for j in self.cars[i]])for i in range(2)]



    def generate_car1(self):
        for i in range(self.n):
            if(i%(self.n/(self.n*self.density))==0):
                self.cars[1][i]=random.randint(0,self.max_v)
        self.current_car_position=[sorted([j for j in self.cars[i]])for i in range(2)]

    # def generate_car(self):
    #     for i in range(self.n):
    #         if(random.random()<self.density):
    #             self.cars[0][i]=random.randint(0,self.max_v)
    #         if(random.random()<self.density):
    #             self.cars[1][i]=random.randint(0,self.max_v)
    #     self.current_car_position=sorted(self.cars.keys())


    def encodecar(self,lane,carposition):
        if carposition<10:
            return str(0)+str(carposition)+','+str(lane)
        else:
            return str(carposition)+','+str(lane)

    def decodecar(self,text):
        info=text.split(',')
        return(int(info[1]),int(info[0]))

    def count_car(self):
        return(sum([len(cars) for cars in self.cars]))

    def flow(self):
        num_site_pass=sum([self.cars[lane][cars] for lane in range(len(self.cars)) for cars in self.cars[lane]])
        if num_site_pass==0:
            return 0
        else:
            return num_site_pass/float(self.n)



    def iteration(self):
        self.current_car_position=[sorted([j for j in self.cars[i]])for i in range(2)]
        encode_car_position=sorted([self.encodecar(i,j) for i in range(2) for j in self.cars[i]])
        for i in encode_car_position[::-1]:
            self.changelane(i)

        encode_car_position=sorted([self.encodecar(i,j) for i in range(2) for j in self.cars[i]])
        for i in encode_car_position[::-1]:
            self.acceleration(i)

        encode_car_position=sorted([self.encodecar(i,j) for i in range(2) for j in self.cars[i]])
        for i in encode_car_position[::-1]:
            self.slowing_down(i)

        encode_car_position=sorted([self.encodecar(i,j) for i in range(2) for j in self.cars[i]])
        for i in encode_car_position[::-1]:
            self.randomization(i)
        copyofroad=self.getroad()

        encode_car_position=sorted([self.encodecar(i,j) for i in range(2) for j in self.cars[i]])

        self.nextcars=[{},{}]
        for i in encode_car_position[::-1]:
            self.car_motion(i)
        self.cars=self.nextcars

        return copyofroad

    def changelane(self,car):
        (lane,carposition)=self.decodecar(car)
        index=self.current_car_position[lane].index(carposition)
        current=self.current_car_position[lane][index%len(self.current_car_position[lane])]
        before=self.current_car_position[lane][(index+1)%len(self.current_car_position[lane])]
        if self.changelane_condition(lane,current,before):
            self.cars[self.otherlane(lane)][current]=self.cars[lane][current]
            self.cars[lane].pop(current)
            self.current_car_position[lane].remove(carposition)
            bisect.insort(self.current_car_position[self.otherlane(lane)],carposition)

    def changelane_condition(self,lane,current,before):
        condition1=(self.cars[lane][current]>self.cars[lane][before])
        condition2=(not current in self.cars[self.otherlane(lane)])
        condition3=(before-current)%self.n<=self.max_v/2
        return (condition1 and condition2 and condition3)

    def otherlane(self,lane):
        return int(not lane)

    def acceleration(self,car):
        (lane,carposition)=self.decodecar(car)
        if(self.cars[lane][carposition]<self.max_v):
            self.cars[lane][carposition]+=1

    def slowing_down(self,car):
        (lane,carposition)=self.decodecar(car)
        index=self.current_car_position[lane].index(carposition)
        current=self.current_car_position[lane][index%len(self.current_car_position[lane])]
        before=self.current_car_position[lane][(index+1)%len(self.current_car_position[lane])]
        if((before-current)%self.n<=self.cars[lane][current] and before!=current):
            self.cars[lane][current]=(before-current)%self.n-1

    def randomization(self,car):
        (lane,carposition)=self.decodecar(car)
        if(random.random()<self.slow_down_random_probability):
            if(not self.cars[lane][carposition]==0):
                self.cars[lane][carposition]-=1

    def car_motion(self,car):
        (lane,carposition)=self.decodecar(car)
        velocity=self.cars[lane][carposition]
        nextposition=(velocity+carposition)%self.n
        self.nextcars[lane][nextposition]=velocity

    def get_car(self):
        return self.cars

    def printroad(self):
        board0=['~' for i in range(self.n)]
        board1=['~' for i in range(self.n)]
        for i in self.cars[0]:
            board0[i]=int(self.cars[0][i])
        for i in self.cars[1]:
            board1[i]=int(self.cars[1][i])
        string=''
        for i in board0:
            string+=str(i)
        string+='\n'
        for i in board1:
            string+=str(i)
        print(string)

    def getroad(self):
        board0=['~' for i in range(self.n)]
        board1=['~' for i in range(self.n)]
        for i in self.cars[0]:
            board0[i]=int(self.cars[0][i])
        for i in self.cars[1]:
            board1[i]=int(self.cars[1][i])
        string=''
        for i in board0:
            string+=str(i)
        string+='\n'
        for i in board1:
            string+=str(i)
        return(string)
