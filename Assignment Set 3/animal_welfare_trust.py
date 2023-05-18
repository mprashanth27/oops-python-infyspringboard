#lex_auth_012751861844041728222 [Assignment on Static Counter - Level 1]

class Parrot:
    __counter=7000
    
    def __init__(self,name,color):
        self.__name=name
        self.__color=color
        Parrot.__counter+=1
        self.__unique_number=Parrot.__counter

    def get_name(self):
        return self.__name


    def get_color(self):
        return self.__color


    def get_unique_number(self):
        return self.__unique_number

p1=Parrot("Ray","Green")
p2=Parrot("Jay","Lemon")
p3=Parrot("Jay3","Lemon3")
p4=Parrot("Jay4","Lemon4")
p5=Parrot("Jay5","Lemon5")
p6=Parrot("Jay6","Lemon6")

print(p6.get_name(),p6.get_color(),p6.get_unique_number())