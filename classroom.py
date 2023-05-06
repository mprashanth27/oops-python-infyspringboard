#lex_auth_012751124968554496166
#Start writing your code here

class Classroom:
    classroom_list=['G015', 'G066', 'L123', 'L135', 'L143', 'L13']
    
    @staticmethod
    def search_classroom(class_room):
        class_room=str(class_room).upper()
        for room in Classroom.classroom_list:
            if (class_room==room and class_room.startswith("L")):
                Value="Found"
                break
            else:
                Value=-1
            
        return Value
    
#Classroom.classroom_list.extend(['G015', 'G066', 'L123', 'L135', 'L143', 'L13'])

#print(Classroom.classroom_list)
print(Classroom.search_classroom("l135"))
#print(Classroom.search_classroom("Phy"))
