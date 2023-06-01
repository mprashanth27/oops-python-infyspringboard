#lex_auth_012751902958862336276 [Assignment on Static List - Level 3]

class Multiplex:
    __list_movie_name=["movie1","movie2"]
    __list_total_tickets=[100,60]
    __list_last_seat_number=[None,None]
    __list_ticket_price=[150,200]
    def __init__(self):
        self.__seat_numbers=None
        self.__total_price=None
    def calculate_ticket_price(self,movie_index,number_of_tickets):
        self.__total_price= Multiplex.__list_ticket_price[movie_index]*number_of_tickets
    def check_seat_availability(self,movie_index,number_of_tickets):
        if(Multiplex.__list_total_tickets[movie_index]<number_of_tickets):
            return False
        else:
            return True
    def get_total_price(self):
        return self.__total_price
    def get_seat_numbers(self):
        return self.__seat_numbers
    def book_ticket(self, movie_name, number_of_tickets):
        '''Write the logic to book the given number of tickets for the specified movie.'''
        #movie_index=Multiplex.__list_movie_name.index(movie_name) #Throwing ValueError: 'movie3' is not in list during runtime & also bypassing below movie name validation 
        if movie_name.lower() not in Multiplex.__list_movie_name:
            return 0
        elif not(self.check_seat_availability(Multiplex.__list_movie_name.index(movie_name), number_of_tickets)):
            return -1
        else:
            self.__seat_numbers=self.generate_seat_number(Multiplex.__list_movie_name.index(movie_name),number_of_tickets)
            self.calculate_ticket_price(Multiplex.__list_movie_name.index(movie_name), number_of_tickets)
        
    def  generate_seat_number(self,movie_index, number_of_tickets):
        '''Write the logic to generate and return the list of seat numbers'''
        seat_numbers_list=[]
        if(movie_index==0):
            for i in range(1,number_of_tickets+1):
                seat_number="M1-"+str(i)
                seat_numbers_list.append(seat_number)
                Multiplex.__list_total_tickets[0]-=1
            Multiplex.__list_last_seat_number[0]=seat_number
        elif(movie_index==1):
            for i in range(1,number_of_tickets+1):
                seat_number="M2-"+str(i)
                seat_numbers_list.append(seat_number)
                Multiplex.__list_total_tickets[1]-=1
            Multiplex.__list_last_seat_number[1]=seat_number
        return seat_numbers_list
                
booking1=Multiplex()
status=booking1.book_ticket("movie1",10)
if(status==0):
    print("invalid movie name")
elif(status==-1):
    print("Tickets not available for movie-1")
else:
    print("Booking successful")
    print("Seat Numbers :", booking1.get_seat_numbers())
    print("Total amount to be paid:", booking1.get_total_price())
print("-----------------------------------------------------------------------------")
booking2=Multiplex()
status=booking2.book_ticket("movie3",5)
if(status==0):
    print("invalid movie name")
elif(status==-1):
    print("Tickets not available for movie-2")
else:
    print("Booking successful")
    print("Seat Numbers :", booking2.get_seat_numbers())
    print("Total amount to be paid:", booking2.get_total_price())