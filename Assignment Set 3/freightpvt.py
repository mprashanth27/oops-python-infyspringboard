#lex_auth_012751865474736128227 [Assignment on Aggregation - Level 2]

class Freight:
    counter=198
    def __init__(self,recipient_customer, from_customer, weight, distance):
        self.__freight_id=None
        self.__recipient_customer=recipient_customer
        self.__from_customer=from_customer
        self.__weight=weight
        self.__distance=distance
        self.__freight_charge=0


    def get_freight_id(self):
        return self.__freight_id

    def get_recipient_customer(self):
        return self.__recipient_customer

    def get_from_customer(self):
        return self.__from_customer

    def get_weight(self):
        return self.__weight

    def get_distance(self):
        return self.__distance

    def get_freight_charge(self):
        return self.__freight_charge

    def validate_weight(self):
        return self.__weight%5==0
    
    def validate_distance(self):
        return self.__distance>=500 and self.__distance<=5000
    
    def forward_cargo(self):
        if(self.__from_customer.validate_customer_id() and self.__recipient_customer.validate_customer_id() and self.validate_distance() and self.validate_weight()):
            Freight.counter+=2
            self.__freight_id=Freight.counter
            self.__freight_charge=150*self.__weight+60*self.__distance
        else:
            self.__freight_charge=0    

class Customer:
    def __init__(self,customer_id, customer_name, address):
        self.__customer_id=customer_id
        self.__customer_name=customer_name
        self.__address=address

    def get_customer_id(self):
        return self.__customer_id

    def get_customer_name(self):
        return self.__customer_name

    def get_address(self):
        return self.__address

    def validate_customer_id(self):
        return self.__customer_id>=100000 and self.__customer_id<=199999
        
        
cust1=Customer(100001,"John","142/1")
cust2=Customer(100002,"Jones","155/1")

f1=Freight(cust2,cust1,50,510)
f1.forward_cargo()

print(f"Freight id-{f1.get_freight_id()}\nFreight charge={f1.get_freight_charge()}")