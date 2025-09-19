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
    # Constructor: it should have the computer attributes as parameters
    # Remember: in python, all constructors have the same name (__init__)
    # Contractor to initialize the attributes
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
        # Removed Pass

    # What methods will you need?
    # For the method I choose to have them into 3 main Partitions.
    #1. Brand-Model-Os
    #2. Display-Memory-Storage
    #3. Battery-Year of Manufacturing-Price
    def DisplayComputerDetails(self):
        print(f'Brand: {self.Brand}, Model: {self.Model}, OS: {self.Os}, Display: {self.Display}, Memory: {self.Memory}, Storage: {self.Storage}, Battery: {self.Battery}, Year of Manufacturing: {self.Year_of_Manufacturing}, Price: ${self.Price}')
    def update_OS(self, new_os):
        self.Os=new_os

    def update_price(self, new_price):
        self.Price=new_price
    