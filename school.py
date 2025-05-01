class StudentDatabase:
    student_list = []
 
class Student(StudentDatabase):
    def __init__(self,name,department):
        self.__id = len(StudentDatabase.student_list)+1
        self.__name= name
        self.__department = department
        self.__is_enrolled = False   

    def add_student(self):
        StudentDatabase.student_list.append(self)

    @classmethod
    def enroll_student(self,id):
        if id < 1 or id > len(self.student_list):
            print('Invalid student ID for enrolling a student.')
        elif self.student_list[id-1].__is_enrolled:
            print('Trying to enroll a student who is already enrolled.')
        else:
            self.student_list[id-1].__is_enrolled = True
            print(f'Enrolment is completed for {self.student_list[id-1].__name}')

    @classmethod
    def drop_student(self,id):
        if id < 1 or id > len(self.student_list):
            print('Invalid student ID for dropping a student.')
        elif not self.student_list[id-1].__is_enrolled:
            print('Trying to drop a student who is not enrolled.')
        else:
            self.student_list[id-1].__is_enrolled = False
            print(f'drop out {self.student_list[id-1].__name}')
    
    @classmethod
    def view_student_info(self):
        if len(self.student_list)<=0:
            print('There has No Student.')
        else:
            for student in self.student_list:
                print(f'ID: {student.__id}, Name: {student.__name}, Department: {student.__department}, Enrolled: {student.__is_enrolled}')
        

anis = Student('Anis','science')
anis.add_student()
fahim = Student('Fahim','science')
fahim.add_student()

while True:
    print('---------Student Management Menu------------')
    print('1. View All Students\n2. Enroll Student\n3. Drop Student\n4. Exit')
    num = int(input('Enter Your choice: '))
    if num == 1:
        Student.view_student_info()
    elif num == 2:
        id = int(input('Give ID: '))
        Student.enroll_student(id)
    elif num==3:
        id = int(input('Give ID: '))
        Student.drop_student(id)
    elif num==4 or num > 4 or num <1:
        break
    print()
