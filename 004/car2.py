class Car:
  """자동차를 표현하는 클래스"""

  def __init__(self, make, model, year):
    """자동차 속성 초기화"""
    self.make = make
    self.model = model
    self.year = year
    self.odometer_reading = 0

  def get_descriptive_name(self):
    """뜻이 분명하고 깔끔한 이름 반환"""
    long_name = f"{self.year} {self.make} {self.model}"
    return long_name.title()
  
  def read_odometer(self):
   """자동차의 주행거리를 출력합니다"""
   print(f"This car has {self.odometer_reading} miles on it.")

  def update_odometer(self, mileage):
    """거리계를 주어진 값으로 설정합니다"""
    self.odometer_reading = mileage


my_new_car = Car("audi", 'a4', 2024)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

my_new_car.odometer_reading = 23
my_new_car.read_odometer() #속성 값 직접 수정하기

my_new_car.update_odometer(42)
my_new_car.read_odometer() #메소드를 통해 속성 값 직접 수정하기

class Battery:
  """전기차의 배터리를 표현하는 클래스"""
  def __init__(self, battery_size=40):
    self.battery_size = battery_size

  def describe_battery(self):
    """배터리 크기를 설명하는 문장을 출력합니다"""
    print(f'This car has a {self.battery_size}-kWh battery.')

class ElectricCar(Car): # 부모 클래스 상속받기
  """전기차에만 해당하는 특징을 정의합니다"""

  def __init__(self, make, model, year):
    super().__init__(make, model, year)
    """부모 클래스의 속성을 초기화 합니다"""
    self.battery = Battery()
  
  def fill_gas_tank(self):
    """전기차에는 연료통이 없습니다"""
    print("This car doesn't have a gas tank !")

my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()



