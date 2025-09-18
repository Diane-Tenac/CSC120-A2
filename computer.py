class Computer:

    # What attributes will it need? This will need Brand,Model, Os, Display, Memory, storage, Battery, Year of Manufcturing and Price
    # computer attributes
    Brand:str
    Model:str
    Os:str
    Display:str
    Memory:str
    Storage:str
    Battery:str
    Year_of_Manufacturing:int
    Price:int


    # How will you set up your constructor?
    # Constructor: it should have the computer attributes not as parameters
    def __init__(self, Brand, Model, Os, Display, Memory, Storage, Battery, Year_of_Manufacturing, Price):
        self.Brand=Brand
        self.Model=Model
        self.Os=Os
        self.Display=Display
        self.Memory=Memory
        self.Storage=Storage
        self.Battery=Battery
        self.Year_of_Manufacturing=Year_of_Manufacturing
        self.Price=Price


    # Remember: in python, all constructors have the same name (__init__)
    def __init__():
        pass # You'll remove this when you fill out your constructor

    # What methods will you need?
    # For the method I choose to have them into 3 main Partitions.
    #1. Brand-Model-Os
    #2. Display-Memory-Storage
    #3. Battery-Year of Manufacturing-Price
    def BrandModelOs():
         # Not sure what to put here yet
         pass
    def DisplayMemoryStorage():
         # Not sure what to put here yet
         pass
    def BatteryYearOfManufacturingPrice():
         # Not sure what to put here yet
         pass