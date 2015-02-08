class Car(object):
    def __init__(self):
        self.manufacturer = None
        self.model = None
        self.year = None
        self.bhp = None
        self.price = None
        self.zerotosixty = None
        self.topspeed = None
#Manufacturer, Model, Bhp, 0-60, Top Speed, Price        
        

db =[
        ["Vector","Avtech WX8",1250, 2.6 "seconds", 270 "mph", "$"1500000   ],
        

        
     ]       

list_of_cars = []
for i in range(2):
    s = input("Manufacturer, Model, Bhp, 0-60, Top Speed, Price")
    c = Car()
    c.manufacturer, c.model, c.bhp, c.zerotosixty, c.topspeed, c.price = s.split(",")
    list_of_cars.append(c)
    
    
    
