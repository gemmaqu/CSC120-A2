from typing import Optional

from computer import Computer


class ResaleShop:

    # What attributes will it need?
    inventory:list

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self,inventory:list):
        if inventory is None:
            self.inventory = []
        self.inventory = inventory

    def print_inventory(self):
    # If the inventory is not empty
        if self.inventory:
            # For each item
            for item in self.inventory:
                # Print its details
                print(f'Item ID: {self.inventory.index(item)} : {item.description,item.processor_type,item.hard_drive_capacity,item.memory,item.operating_system,item.year_made,item.price}')
        else:
            print("No inventory to display.")

    

    def update_price(self,item_id: int, new_price: int):
        if item_id in self.inventory:
            self.inventory[item_id]["price"] = new_price
        else:
            print("Computer", item_id, "not found. Cannot update price.")
    
    def sell(self,item_id: int):
        if self.inventory[item_id] is not None:
            self.inventory.pop(item_id)
            print("Computer", item_id, "sold!")
        else: 
            print("Computer", item_id, "not found. Please select another item to sell.")

    def buy(self,computer:Computer):
        self.inventory.append(computer)
        
    
    

    def update_os(self,item_id: int, new_os: int):
        if len(self.inventory) > item_id and self.inventory[item_id] is not None:
            self.inventory[item_id]["os"] = new_os
        else:
            print("Item", item_id, "not found. Cannot update price.")

    def refurbish(self,item_id: int, new_os: Optional[str] = None):
        if self.inventory[item_id] is not None:
            computer = self.inventory[item_id] # locate the computer
            if int(computer.year_made) < 2000:
                computer.price = 0 # too old to sell, donation only
            elif int(computer.year_made) < 2012:
                computer.price = 250 # heavily-discounted price on machines 10+ years old
            elif int(computer.year_made) < 2018:
                computer.price = 550 # discounted price on machines 4-to-10 year old machines
            else:
                computer.price = 1000 # recent stuff

            if new_os is not None:
                computer.operating_system = new_os # update details after installing new OS
        else:
            print("Item", item_id, "not found. Please select another item to refurbish.")


def main():
    
    comp1 = Computer("Dell XPS 15", "Intel i7", 512, 16, "Windows 10", 2020, 1500)
    comp2 = Computer("MacBook Pro", "Intel i5", 256, 8, "macOS", 2017, 1200)
    comp3 = Computer("HP Pavilion", "AMD Ryzen 5", 1024, 16, "Windows 10", 2019, 1100)
    
 
    shop = ResaleShop([])  
    
    
    shop.buy(comp1) 
    shop.buy(comp2)  
    shop.buy(comp3) 
    
  
    print("\nInventory after buying computers:")
    shop.print_inventory()
    
   
    print("\nRefurbishing computer with ID 2 (MacBook Pro):")
    shop.refurbish(2) 
    shop.print_inventory()

   
    print("\nUpdating price of computer with ID 1 (Dell XPS 15):")
    shop.update_price(1, 1400) 
    shop.print_inventory()


    print("\nUpdating OS of computer with ID 3 (HP Pavilion):")
    shop.update_os(3, "Ubuntu Linux")  # Changing OS of the HP Pavilion
    shop.print_inventory()

    
    print("\nSelling computer with ID 2 (MacBook Pro):")
    shop.sell(2)
    shop.print_inventory()



if __name__ == "__main__":
    main()
