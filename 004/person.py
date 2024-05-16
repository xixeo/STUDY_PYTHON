class Person:
  def __init__(self, pid, pname, age):
    self.pid = pid
    self.pname = pname
    self.age = age

  def describe_person(self):
    print(f'id = {self.pid}, name = {self.pname}, age = {self.age}')
  
class Dept:
  def __init__(self, depart):
    self.depart = depart

class Student(Person, Dept):
    def __init__(self, pid, pname, age, sid, syear, depart):
      Person.__init__(self, pid, pname, age)
      Dept.__init__(self, depart)
      self.sid = sid
      self.syear = syear

    def describe_student(self):
      print(f'id = {self.pid}, name = {self.pname}, age = {self.age} id = {self.sid}, year = {self.syear}, department = {self.depart}')


s1 = Student(1, 'jang', 30, 1, 2024, 'computer')
s2 = Student(2, 'bang', 30, 2, 2024, 'computer')
s3 = Student(3, 'kang', 30, 3, 2024, 'computer')

p1 = Person(1, 'baek', 31)
p2 = Person(2, 'jack', 38)
p3 = Person(3, 'gwak', 45)
# p1.describe_person()

studentList = [s1, s2, s3]
personList = [p1, p2, p3]
# for student in studentList:
#   student.describe_student()

# for person in personList:
#   person.describe_person()

mergeList = [*studentList, *personList]

for item in mergeList:
    if isinstance(item, Student):
        item.describe_student()
    elif isinstance(item, Person):
        item.describe_person()