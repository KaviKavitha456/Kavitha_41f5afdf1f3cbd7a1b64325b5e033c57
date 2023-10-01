class Student:
  def __init__(self, name, rollnumber, cgpa):
    self.name = name
    self.rollnumber = rollnumber
    self.cgpa = cgpa
def sortstudents(studentlist):
  sortedstudents = sorted(studentlist,
                           key=lambda student: student.cgpa, reverse=True)
  return sortedstudents
students = [
   Student("kavitha","37", 10),
    Student("karthik", "73", 11),
    Student("kaviya", "78", 12),
    Student("divya", "79", 13)]

sortedstudents = sortstudents(students)
for student in sortedstudents:
  print("Name: {}; Roll Number: {}; CGPA: {}".format(student.name,
student.rollnumber,                    student.cgpa)); 
