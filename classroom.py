#lex_auth_012751124968554496166
#Start writing your code here

class Classroom:
    classroom_list=[]
    
    @staticmethod
    def search_classroom(class_room):
        for room in Classroom.classroom_list:
            if str(class_room).upper()==room.upper():
                return "Found"
            else:
                return -1
            
Classroom.classroom_list.extend(['G015', 'G066', 'L123', 'L135', 'L143', 'L13'])

#print(Classroom.classroom_list)
print(Classroom.search_classroom(13))
#print(Classroom.search_classroom("Phy"))