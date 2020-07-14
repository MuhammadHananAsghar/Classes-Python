class Car:
    def __init__(self,make = "unknown",model="unknown",color="unknown",year = -1,price = -1):
        self.make = make
        self.model = model
        self.color = color
        self.year = year
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self,p):
        if(p <= 0):
            raise ValueError("Value is Less Than Zero or Zero")
        self._price = p 
    
    def __str__(self):
        return "Car(make = "+self.make+","+"model = "+str(self.model)+")"

car = Car(model = "Ferrari")
car.price = 1000
car2 = Car("lusibese","buick")
print("Model : ",car.model)
print("Price :  ",car.price)
print(car)
fh = open("cars.csv","r")
car_Data = fh.readlines()
car_Data.pop(0)
car_list = []
for rawstr in car_Data:
    make,model,color,year,price = rawstr.split(",")
    car_list.append(Car(make,model,color,year,price))

car_list.sort(key = lambda car : car.price)
print(*car_list , sep="   ---------->>>>>   ")