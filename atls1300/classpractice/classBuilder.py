class Car():
    # class attributes (shared by all objects)
    windshield = True
    
    # instance attributes (switch em up as you please!)
    def __init__(self, color, drive="2WD", doors=2):
        # features that are not shared by all objects
        self.color = color
        self.drive = drive
        self.doors = doors
        
    def go(self):
        print(self.drive)

class SUV(Car):
    def __init__(self,color):
        super().__init__(color, drive="4WD",doors=4) # gives complete inheritance of instance attributes and methods
        self.height = 4

    def go(self): # overwrite parent method go()
        print("crawl")

    def camp(self):
        print("lock the doors at night.")

suv = SUV("maroon")       
print(suv.doors) # child class attribute 
print(suv.drive)
suv.go() # parent method
suv.camp()


coupe = Car("black", doors=2)
coupe.go()
coupe.camp()

# see values stored to object with dot notation
print(coupe.doors)
print(suv.doors)


print(coupe.doors)
print(suv.doors)


class Car:
    # class attributes (shared by all objects)
    doors = 4
    drive = "AWD"
    color = "red"

suv = Car()
coupe = Car()
coupe.doors = 2 # build the car, then remove the doors
coupe.color = "black" # paint the car, then paint over it

# see values stored to object with dot notation
print(coupe.doors)
# print(suv.doors)