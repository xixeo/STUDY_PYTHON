class Dog:
  """개를 표현하는 클래스"""

  def __init__(self, name, age): # underline __ 은 자동호출한다는 특별한 의미를 가지고 있다. 
    """name과 age 속성 초기화"""
    self.name = name
    self.age = age
    self.city = "city" #파라미터가 없어서 고정값

  def sit(self):
    """앉기"""
    print(f"{self.name} is now sitting.")

  def roll_over(self):
    """구르기"""
    print(f"{self.name} rolled over !")

my_dog = Dog("alex", 10)
my_dog.sit()

print(f"My Dog's name is {my_dog.name}")
print(f"My dog is {my_dog.age} years old")
print(f"My dog is from {my_dog.city}")
