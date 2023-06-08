#lex_auth_012753087522512896330 [Assignment on Inheritance - Level 2]

class Apparel:
    counter=100
    def __init__(self,price,item_type):
        self.__item_id=None
        self.__price=float(price)
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

    def set_price(self, price):
        self.__price = price

    def calculate_price(self):
        self.__price*=1.05

class Cotton(Apparel):
    def __init__(self,price,discount):
        super().__init__(price, "Cotton")
        self.__discount=float(discount)
    
    def get_discount(self):
        return self.__discount
    
    def calculate_price(self):
        super().calculate_price()
        price=self.get_price()
        Final_price=1.05*(price)*(1-self.__discount/100) #discount & 5% VAT on final price
        self.set_price(Final_price)
    
class Silk(Apparel):
    def __init__(self,price):
        super().__init__(price, "Silk")
        self.__points=0 #Needed??
            
    def get_points(self):
        return self.__points
    
    def calculate_price(self):
        super().calculate_price()
        
        if 0<=self.get_price()<=10000:
            self.__points+=3
        elif self.get_price()>10000:
            self.__points+=10
        
        self.set_price(1.1*self.get_price()) #10% VAT on price
        
c1=Cotton(500,10)
s1=Silk(1000)

c1.calculate_price()
s1.calculate_price()

print(f"Cotton Apparel:\ndiscount={c1.get_discount()}\nFinal price={c1.get_price()}")
print(f"Silk Apparel:\npoints={s1.get_points()}\nFinal price={s1.get_price()}")
            
        