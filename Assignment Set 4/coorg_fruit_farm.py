#lex_auth_012753080343093248327 [Assignment on Dependency & Aggregation - Level 3]

class FruitInfo:
    __fruit_name_list=["Apple","Guava","Orange","Grape","Sweet Lime"] #list of fruits available
    __fruit_price_list=[100, 800, 70, 110, 600] #price/kg of fruits

    @staticmethod
    def get_fruit_name_list():
        return FruitInfo.__fruit_name_list

    @staticmethod
    def get_fruit_price_list():
        return FruitInfo.__fruit_price_list
    
    @staticmethod
    def get_fruit_price(fruit_name):
        if fruit_name in FruitInfo.__fruit_name_list:
            return FruitInfo.__fruit_price_list[FruitInfo.__fruit_name_list.index(fruit_name)]
        return -1
    
class Customer:
    def __init__(self,customer_name,cust_type):
        self.__customer_name=customer_name
        self.__cust_type=cust_type

    def get_customer_name(self):
        return self.__customer_name

    def get_cust_type(self):
        return self.__cust_type    
        

class Purchase:
    __counter=101
    def __init__(self,customer,fruit_name,quantity):
        self.__purchase_id=None
        self.__customer=customer
        self.__fruit_name=fruit_name
        self.__quantity=quantity

    def get_purchase_id(self):
        return self.__purchase_id

    def get_customer(self):
        return self.__customer

    def get_quantity(self):
        return self.__quantity

    def calculate_price(self):
        fruit_price=FruitInfo.get_fruit_price(self.__fruit_name)
        if fruit_price==-1:
            return -1
        else:
            final_price=self.__quantity*fruit_price
            if fruit_price==max(FruitInfo.get_fruit_price_list()) and self.__quantity>1:
                final_price*=0.98
            elif fruit_price==min(FruitInfo.get_fruit_price_list()) and self.__quantity>=5:
                final_price*=0.95
            
            if self.__customer.get_cust_type()=="wholesale":
                final_price*=0.9
            
            self.__purchase_id="P"+str(Purchase.__counter)
            Purchase.__counter+=1
            return final_price

c1=Customer("Tom","wholesale")
p1=Purchase(c1,"Guava",1)
print(p1.calculate_price())
        
        