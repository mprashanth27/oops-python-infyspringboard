#lex_auth_012751878508396544244 [Assignment on Static - Level 2]

class Applicant:
    __application_dict={'A':0,'B':0,'C':0}
    __applicant_id_count=1000
    def __init__(self,applicant_name):
        self.__applicant_id=0
        self.__applicant_name=applicant_name
        self.__job_band=None
    
    @staticmethod
    def get_application_dict():
        return Applicant.__application_dict

    def get_applicant_id(self):
        return self.__applicant_id

    def get_applicant_name(self):
        return self.__applicant_name

    def get_job_band(self):
        return self.__job_band

    def generate_applicant_id(self):
        Applicant.__applicant_id_count+=1
        self.__applicant_id=Applicant.__applicant_id_count
        
    def apply_for_job(self,job_band):
        if str(job_band).isalpha() and job_band!=None: #Added this Error check to satisfy test cases but no luck; remove this later if not required
            if Applicant.__application_dict[job_band]>=5:
                print("applied job band has reached the maximum limit!")
                return -1
            else:
                Applicant.__application_dict[job_band]+=1
                self.generate_applicant_id()
                self.__job_band=job_band
                print(f"applicant_id:{self.__applicant_id}\napplicant_name:{self.__applicant_name}\njob band:{self.__job_band}")
        else:
            return -1
            
a=Applicant("Jack")
a1=Applicant("John1")
a2=Applicant("John2")
a3=Applicant("John3")

a.apply_for_job("A")
a1.apply_for_job("A")
#a1.apply_for_job(A) #why is this wrong getting NameError: name 'A' is not defined
a2.apply_for_job("A")
a3.apply_for_job("B")
