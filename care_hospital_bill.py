#lex_auth_012727139457941504148
#Start writing your code here

class Bill:
    def __init__(self,bill_id,patient_name):
        self.__bill_id=bill_id
        self.__patient_name=patient_name
        self.__bill_amount=0
    
    def get_bill_id(self):
        return self.__bill_id

    def get_patient_name(self):
        return self.__patient_name

    def get_bill_amount(self):
        return self.__bill_amount


    def calculate_bill_amount(self,consultation_fees, quantity_list, price_list):
        med_price=0
        for i in range(len(quantity_list)):
            med_price+=quantity_list[i]*price_list[i]
            
        self.__bill_amount+=(consultation_fees+med_price)
    
b1=Bill(100,"John")
b1.calculate_bill_amount(500, [5,5,5], [5,5,5])    

print(f"bill_id:{b1.get_bill_id()}\npatient_name:{b1.get_patient_name()}\nbill_amount:{b1.get_bill_amount()}")  