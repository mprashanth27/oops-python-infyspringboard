#lex_auth_012753087522512896330 [Assignment on Inheritance - Level 2]

class Apparel:
    counter=100
    def __init__(self,price,item_type):
        self.__item_id=0 #Needed??
        self.__price=price
        self.__item_type=item_type
        
        if self.__item_type=="Cotton":
            Apparel.counter+=1
            self.__item_id="C"+str(Apparel.counter)
        elif self.__item_type=="Silk":
            Apparel.counter+=1
            self.__item_id="S"+str(Apparel.counter)

    def get_item_id(self):
        return self.__item_id

    def get_price(self):
        return self.__price

    def get_item_type(self):
        return self.__item_type

    def set_price(self, value):
        self.__price = value

    def calculate_price(self):
        self.__price*=1.05

class Cotton(Apparel):
    def __init__(self,price,discount):
        super().__init__(price, "Cotton")
        self.__discount=discount
        
    def calculate_price(self):
        super().calculate_price()
        self.__price-=self.__discount/100*self.__price
        self.__price*=1.05
    
class Silk(Apparel):
    def __init__(self,price):
        super().__init__(price, "Silk")
        self.__points=0 #Needed??
            
    def get_points(self):
        return self.__points
    
    def calculate_price(self):
        super().calculate_price()
        
        if self.__price<=10000:
            self.__points+=3
        elif self.__points>10000:
            self.__points+=10
        
        self.__price*=1.1
            
        