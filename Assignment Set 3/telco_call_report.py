#lex_auth_01275802761392128033 [Assignment on Dependency - Level 2]

class Customer:
    def __init__(self,phone_no,name,age):
        self.phone_no=phone_no
        self.name=name
        self.age=age
        self.list_of_calls=None

class CallDetail:
    def __init__(self,phone_no,called_no,duration):
        self.phone_no=phone_no
        self.called_no=called_no
        self.duration=duration

class Util:
    def __init__(self):
        self.list_of_customer_calldetail_objects=[]
        
    def parse_customer(self,list_of_customers,list_of_calls):
        for customer in list_of_customers:
            temp=[]
            for call in list_of_calls:
                if customer.phone_no==call.phone_no:
                    temp.append(call)
            '''if(len(temp)!=0): #IF I DO THIS ERROR CHECK, THE LAST TEST CASE IS FAILING 
                customer.list_of_calls=temp'''
            customer.list_of_calls=temp
            self.list_of_customer_calldetail_objects.append(customer)
            
    def display(self):
        for i in self.list_of_customer_calldetail_objects:
            print("***",i.__dict__,"***") #Will display the value of customer obj's stored in self.list_of_customer_calldetail_objects attribute
            for j in i.list_of_calls:
                print(j.__dict__) #Will display the value of calldetail_objects obj's stored in list_of_calls attribute of the customer         
                    

cust1=Customer(9900009901,'cust1',23)
cust2=Customer(9900009902,'cust2',24)
cust3=Customer(9900009903,'cust3',25)
list_of_customers=[cust1,cust2,cust3]

call1=CallDetail(9900009901,8800123401,5)
call2=CallDetail(9900009903,8800123402,10)
call3=CallDetail(9900009902,8800123403,2)
call4=CallDetail(9900009901,8800123404,8)
call5=CallDetail(9900009901,8800123405,7)
call6=CallDetail(9900009903,8800123406,9)
call7=CallDetail(9900009903,8800123407,4)
list_of_calls=[call1,call2,call3,call4,call5,call6,call7]

u1=Util()
u1.parse_customer(list_of_customers, list_of_calls)
u1.display()
#print(u1.__dict__)
#print(cust1.list_of_calls)