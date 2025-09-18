import computer.py
class ResaleShop:

    # What attributes will it need?
    # I think attributes here will be mostly what the shop has
    ComputerBrands:str # I think each brand shall also have all the necessary computer attribures in the store.
    BrandCounts:int


    # How will you set up your constructor?
    def __init__(self, ComputerBrands, BrandCounts):
        self.ComputerBrands=ComputerBrands
        self.BrandCounts=BrandCounts
    # Remember: in python, all constructors have the same name (__init__)
    def __init__():
        pass # You'll remove this when you fill out your constructor

    # What methods will you need?
    # I think methods here will be mostly about updating the inventory based on the computer information
    def UpdateInventory():
        # Not sure what to put here yet
        pass
    def CheckinComputer(Brand, Model, Os, Display, Memory, Storage, Battery, Year_of_Manufacturing, Price ):
        # thinking of updating counts +1 whaen a computer is checked in but in a way that it will be recording information based on brands
        # I have got an idea of having something like a list/dictionary that can store computer information and use conditions to recors them based on the brands/other attributes like OS, Model etc.
        # To Keep it simple for now, I will just update the counts +1
        
        self.BrandCounts+=1

        # Not sure what to put here yet
        pass
    def CheckoutComputer():
        # Not sure what to put here yet
        self.BrandCounts-=1
        pass
    #### I want to use boolean for checking if there are transactions made like checkin/checkout, so I can use that to update the inventory but I am stuck in ideas.
   