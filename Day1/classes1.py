
class Student:
    def __init__(self):
        self.FirstName=""
        self.LastName ="" 
        self.DOB="00/00/0000"

    def __str__(self):
        return f"{self.FirstName} {self.LastName} dob = {self.DOB}"
    
class GraduatedStudent(Student):
    pass 

def main():
    Leo = GraduatedStudent()
    Leo.FirstName="Leonardo"

    Marco = Student()
    Marco.FirstName="Marco"

    print(Leo)
    print(Marco)
    # pass

if __name__=="__main__":
    main()