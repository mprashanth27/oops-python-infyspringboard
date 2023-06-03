#lex_auth_0127475574441738242319 [Exercise on Inheritance - Level 1]

class Rider:
    def __init__(self,trained_status,experience):
        self.__trained_status=trained_status
        self.__experience=experience
        
    def rides_vehicle(self):
        print("Rider rides vehicle")
    
class BikeRider(Rider):
    def __init__(self,trained_status,experience,race_license):
        super().__init__(trained_status, experience)
        self.__race_license=race_license
        
    def rides_in_dome(self):
        print("Bike Rider rides in dome")
        
class CycleRider(Rider):
    def rides_blindfolded(self):
        print("Cycle Rider rides blindfolded")
        
b1=BikeRider(True,8,True)
b1.rides_in_dome()

c1=CycleRider(True,5)
c1.rides_vehicle()
c1.rides_blindfolded()