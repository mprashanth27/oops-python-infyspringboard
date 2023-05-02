#lex_auth_012736349701922816604
#Start writing your code here

class Vehicle:
    def __init__(self):
        self.__vehicle_id=None
        self.__vehicle_type=None
        self.__vehicle_cost=None
        self.__premium_amount=None

    def set_vehicle_id(self,vehicle_id):
        self.__vehicle_id=vehicle_id
    def get_vehicle_id(self):
        return self.__vehicle_id

    def set_vehicle_type(self, vehicle_type):
        if(vehicle_type=="Two Wheeler" or vehicle_type=="Four Wheeler"):
            self.__vehicle_type=vehicle_type
        else:
            print("Invalid vehicle type")
    def get_vehicle_type(self):
        return self.__vehicle_type

    def set_vehicle_cost(self,vehicle_cost):
        self.__vehicle_cost=vehicle_cost
    def get_vehicle_cost(self):
        return self.__vehicle_cost

    def set_premium_amount(self, premium_amount):
        self.__premium_amount=premium_amount
    def get_premium_amount(self):
        return self.__premium_amount


    def calculate_premium(self):
        premium_percentage=0
        if(self.get_vehicle_type()=="Two Wheeler"):
            premium_percentage+=2/100
        elif(self.get_vehicle_type()=="Four Wheeler"):
            premium_percentage+=6/100
        else:
            print("Invalid vehicle type")

        self.set_premium_amount((premium_percentage*self.get_vehicle_cost()))

    def display_vehicle_details(self):
        self.calculate_premium()
        print("vehicle_id= "+str(self.get_vehicle_id())+"\nvehicle_type= "+str(self.get_vehicle_type())+"\nvehicle_cost= "+str(self.get_vehicle_cost())+"\npremium_amount= "+str(self.get_premium_amount()))

V1=Vehicle()
V1.set_vehicle_id(101)
V1.set_vehicle_type("Two Wheeler")
V1.set_vehicle_cost(50000)
V1.display_vehicle_details()