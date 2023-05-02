#lex_auth_012748317267525632347 [Exercise on Static Counter - Level 2]

class Ticket:
    counter=0
    
    def __init__(self,passenger_name,source,destination):
        self.__passenger_name=passenger_name
        self.__source=source
        self.__destination=destination
        self.__ticket_id=None

    def get_passenger_name(self):
        return self.__passenger_name


    def get_source(self):
        return self.__source


    def get_destination(self):
        return self.__destination


    def get_ticket_id(self):
        return self.__ticket_id


    def set_passenger_name(self, passenger_name):
        self.__passenger_name = passenger_name


    def set_source(self, source):
        self.__source = source


    def set_destination(self, destination):
        self.__destination = destination


    def set_ticket_id(self, ticket_id):
        self.__ticket_id = ticket_id

    
    def validate_source_destination(self):
        if(self.__source.upper()=="DELHI"):
            if(self.__destination.upper() in ["MUMBAI","CHENNAI","PUNE","KOLKATA"]):
                return True
            else:
                return False
        else:
                return False
    
    def generate_ticket(self):
        if(self.validate_source_destination()):
            Ticket.counter+=1
            if(Ticket.counter<10):
                self.__ticket_id=self.__source[0]+self.__destination[0]+"0"+str(Ticket.counter)
            else:
                self.__ticket_id=self.__source[0]+self.__destination[0]+str(Ticket.counter)
        else:
            self.__ticket_id=None
    
T1=Ticket("John","Delhi","Pune")
T1.generate_ticket()
print(T1.get_ticket_id(),
T1.get_passenger_name(),
T1.get_source(),
T1.get_destination())