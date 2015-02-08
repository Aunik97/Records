#rev ex 1

class StudentMark():
    def __init__(self):
        self.name = None
        self.marks = None

    def capture(self):
        self.name = input("please enter student name")
        self.marks = int(input("marks out of 100"))


    def __repr__(self):
        return "({0},{1})".format(self.name, self.marks)
        

                         
lists = []        
for count in range(2):
    student = StudentMark()
    student.capture()
    lists.append(student)



print(lists)
    
