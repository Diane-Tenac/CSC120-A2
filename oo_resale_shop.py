from typing import Dict, Optional
import computer.py
class ResaleShop:

    # What attributes will it need?
    # I think attributes here will be mostly what the shop has
    computerID:int=0
    inventory:Dict[int,Dict]={} #This is a a dictionary to store the computers linformation with specific key .


    # How will you set up your constructor?
    
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self)->None:
        self.computerID=0

    # What methods will you need?
    # I think methods here will be mostly about updating the inventory based on the computer information
    # thinking of updating counts +1 whaen a computer is checked in but in a way that it will be recording information based on brands
    # I have got an idea of having something like a list/dictionary that can store computer information and use conditions to recors them based on the brands/other attributes like OS, Model etc.
    # To Keep it simple for now, I will just update the counts +1
    def ComputerPurchase(self,computer: Dict):
        self.computerID+=1 # updating the dictionary key for each computer added
        self.inventory[self.computerID]=computer # adding the computer information to the inventory dictionary
        return self.computerID
        
        

        
    def ComputerSells(self,computerID:int):
        if computerID in self.inventory:
            del self.inventory[computerID]
            print("Item", computerID, "sold!")
        else: 
            print("Item", computerID, "not found. Select another item to sell.")
        
    def refubish(self,computerID:int,new_os: Optional[str] = None):
        if self.inventory[computerID] is not None:
            computer = self.inventory[computerID] # located the computer
            if int(computer["year_made"]) < 2015:
                computer["price"] = 0 # too old to sell, donation only
            elif int(computer["year_made"]) < 2018:
                computer["price"] = 250 # heavily-discounted price on machines 10+ years old
            elif int(computer["year_made"]) < 2020:
                computer["price"] = 550 # discounted price on machines 4-to-10 year old machines
            else:
                computer["price"] = 1000 # recent stuff

            if new_os is not None:
                computer.update_os(new_os) # updated details after installing new OS
        else:
            print("Item", computerID, "not found. Please select another item to refurbish.")
def print_inventory(self):
        # Printing all the items in the store
    if self.inventory:
        for computerID in self.inventory:
            print(self.inventory[computerID])
    else:
        print("No inventory to display.")

