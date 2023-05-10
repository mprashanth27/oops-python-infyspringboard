#lex_auth_01275044879016755225
#Start writing your code here

class Vehicle:
    reserve_fuel=5
    
    def __init__(self,mileage,fuel_left):
        self.mileage=mileage
        self.fuel_left=fuel_left
    
    def identify_distance_that_can_be_travelled(self):
        if(self.fuel_left>Vehicle.reserve_fuel):
            return (self.fuel_left-Vehicle.reserve_fuel)*self.mileage
        else:
            return 0
    
    def identify_distance_travelled(self,initial_fuel):
        return (initial_fuel-self.fuel_left)*self.mileage

v1=Vehicle(15,10)
print("Distance before reserve = {0} kms".format(v1.identify_distance_that_can_be_travelled()))
