#lex_auth_012727119215337472135 [Assignment on OOP Basics - Level 2]

class Flower:
    Inventory={"ORCHID":15,"ROSE":25,"JASMINE":40}
    
    def __init__(self):
        self.__flower_name=None
        self.__price_per_kg=None
        self.__stock_available=None

    def get_flower_name(self):
        return self.__flower_name


    def get_price_per_kg(self):
        return self.__price_per_kg


    def get_stock_available(self):
        return self.__stock_available


    def set_flower_name(self, flower_name):
        self.__flower_name = flower_name


    def set_price_per_kg(self, price_per_kg):
        self.__price_per_kg = price_per_kg


    def set_stock_available(self, stock_available):
        self.__stock_available = stock_available

    def validate_flower(self):
        if(self.__flower_name.upper() in Flower.Inventory.keys()): #wt to do if dict is removed
            return True
        else:
            return False
        
    def validate_stock(self,required_quantity):
        if(required_quantity<=self.__stock_available):
            return True
        else:
            return False
    
    def sell_flower(self,required_quantity):
        if(self.validate_flower() and self.validate_stock(required_quantity)):
            self.__stock_available-=required_quantity
    
    def check_level(self):
        if(self.validate_flower()):
            if(self.__stock_available<Flower.Inventory[self.__flower_name.upper()]):
                return True
        else:
            return False
        
f1=Flower()
f1.set_flower_name("Orchid")   
f1.set_price_per_kg(10)
f1.set_stock_available(20)


f1.sell_flower(6)
print(f1.check_level())
