# class Student:
#     def __init__(self,student_name,student_id):
#         self.name = student_name
#         self.id = student_id
#         self.grades ={"语文":0,"数学":0,"英语":0}
        
#     def set_grade(self,course,grade):
#         if course in self.grades:
#             self.grades[course] = grade
            
#     def print_grades(self):
#         print(f"{self.name}(学号是{self.id})的成绩为：")
#         for course in self.grades:
#             print(f"{course}:{self.grades[course]}分")

# li = Student("lyy","202140210221")
# xiong = Student("xsz","202140210224")
# print(li.name)
# xiong.set_grade("语文",80)
# xiong.set_grade("数学",90)
# xiong.print_grades()