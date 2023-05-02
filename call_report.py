#lex_auth_012727085763518464103 [Assignment on List of Objects - Level 1]
#Start writing your code here
class CallDetail:
    def __init__(self,phoneno,called_no,duration,call_type):
        self.__phoneno=phoneno
        self.__called_no=called_no
        self.__duration=duration
        self.__call_type=call_type
        

class Util:
    def __init__(self):
        self.list_of_call_objects=None

    def parse_customer(self,list_of_call_string):
        call_obj_list=[]
        for i in range(len(list_of_call_string)):
            temp=list_of_call_string[i].split(",")
            call_obj=CallDetail(temp[0],temp[1],temp[2],temp[3])
            call_obj_list.append(call_obj)
          
        self.list_of_call_objects=call_obj_list

call='9990000001,9330000001,23,STD'
call2='9990000001,9330000002,54,Local'
call3='9990000001,9330000003,6,ISD'

list_of_call_string=[call,call2,call3]
u1=Util()
u1.parse_customer(list_of_call_string)

print(u1.list_of_call_objects)
#print(u1.list_of_call_objects[0].__dict__)