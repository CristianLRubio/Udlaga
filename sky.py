import random


class Sky:
    def __init__(self, width, height, quantity):
        self.stars=[]
        self.width=width
        self.height=height
        
        for i in range(quantity):
            x=random.randint(0,width)
            y=random.randint(0,height)
            
            self.stars.append([x,y])
            
    def move(self):
        for start in self.stars:
            start[1]+=1
            if start[1]>self.height:
                start[1]=0
