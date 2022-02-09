class Vehicle:
    def __init__(self,color,make,model):
        self.color = color
        self.model = model
        self.make = make

    def print_info(self):
        print(self.color,self.make,self.model)


class Car:
    def __init__(self,owner):

        self.owner = owner





class Machine(Car,Vehicle):
    def __init__(self,color,make,model,owner,door):
        Vehicle.__init__(self,color,make,model)
        Car.__init__(self,owner)
        self.door = door

    def print_info(self):
        Vehicle.print_info(self)
        print(self.owner , self.door)

    def add_door(self):
        while self.door < 5:
            self.door += 1






m = Machine('red','japan','toyoto','ehsan',2)


m.print_info()
m.door
m.add_door()
