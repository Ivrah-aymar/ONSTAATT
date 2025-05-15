#Class inheritence

#Bef inh
#Class Inheritance
#Base model with
class Car:
    def __init__(self):
        self.last2num=78
        self.seats=5
    def driving(self):
        print("Driving my ",self.seats," seated car")
        print("my last two num is ",self.last2num)
class newbuy1(Car): 
    def __init__(self):
        super().__init__()
        self.last2num=78
        self.seats=3
    def driving(self):
        print("Driving my ",self.seats," seated car")
        print("my last two num is ",self.last2num)
class newbuy2(Car):
    def __init__(self):
        super().__init__()
        self.last2num=78
        self.seats=2
    def driving(self):
        print("Driving my ",self.seats," seated car")
        print("my last two num is ",self.last2num)
mycar = Car()
mycar.driving()
newbuyo=newbuy1()
newbuyo.driving()
newbuyo2=newbuy2()
newbuyo2.driving()
'''
Driving my  5  seated car
my last two num is  78
Driving my  3  seated car
my last two num is  78
Driving my  2  seated car
my last two num is  78
'''
#remove func driving and init self.last num from newbuy1 and 2
#Class Inheritance
#Base model with
class Car:
    def __init__(self):
        self.last2num=84
        self.seats=5
    def driving(self):
        print("Driving my ",self.seats," seated car")
        print("my last two num is ",self.last2num)
class newbuy1(Car): 
    def __init__(self):
        super().__init__()
#        self.last2num=78
        self.seats=3
#    def driving(self):
#        print("Driving my ",self.seats," seated car")
#        print("my last two num is ",self.last2num)
class newbuy2(Car):
    def __init__(self):
        super().__init__()
#        self.last2num=78
        self.seats=2
#    def driving(self):
#        print("Driving my ",self.seats," seated car")
#        print("my last two num is ",self.last2num)
mycar = Car()
mycar.driving()
newbuyo=newbuy1()
newbuyo.driving()
newbuyo2=newbuy2()
newbuyo2.driving()

'''
Driving my  5  seated car
my last two num is  84
Driving my  3  seated car
my last two num is  84
Driving my  2  seated car
my last two num is  84
'''

