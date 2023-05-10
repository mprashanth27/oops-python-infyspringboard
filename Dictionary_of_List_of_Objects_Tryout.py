"""
We have a list of customer objects. Complete the code so that we have a dictionary of customer objects based on location.
"""

class Customer:
    def __init__(self, cust_id, cust_name, location):
        self.cust_id = cust_id
        self.cust_name = cust_name
        self.location = location

list_of_customers = [Customer(101, 'Mark', 'US'),
Customer(102, 'Jane', 'Japan'),
Customer(103, 'Kumar', 'India'),Customer(104, 'Kumari', 'India')]

dict_of_customer={}
location_list=[]

for customer in list_of_customers:
    if customer.location not in location_list:
        location_list.append(customer.location)
    
#for place in location_list:

for place in location_list:
    dict_of_customer[place]=None

for key in dict_of_customer:
    for customer in list_of_customers:
        if (key==customer.location):
            if(dict_of_customer[key]==None):
                dict_of_customer[key]=[customer]
            else:
                dict_of_customer[key].append(customer)
                
''' I want to add all customer objs as values based on their location; able to add atributes like name,... but not the entire obj.
ERRO - Traceback (most recent call last):
  File "F:\Prashanth disk(f)\VS Code projects\Python\OOPS-Python\Dictionary_of_List_of_Objects_Tryout.py", line 33, in <module>
    dict_of_customer[key]=dict_of_customer[key]+","+customer
TypeError: unsupported operand type(s) for +: 'Customer' and 'str' 
SOLVED IT BY ADDING CUSTOMERS FROM SAME LOCATION INTO A LIST AND PASSING THAT AS THE VALUE TO THE RESPECTIVE KEY(LOCATION)'''

print(dict_of_customer)