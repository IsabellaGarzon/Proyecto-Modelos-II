class Podium:
  def __init__(self):
    self.first_place = None
    self.second_place = None
    self.third_place = None
    
  def set_first_place(self, driver):
    self.first_place = driver
    
  def set_second_place(self, driver):
    self.second_place = driver
    
  def set_third_place(self, driver):
    self.third_place = driver
    
  def get_first_place(self):
    return self.first_place
    
  def get_second_place(self):
    return self.second_place
    
  def get_third_place(self):
    return self.third_place
  
  def clean_podium(self):
    self.set_first_place(None)
    self.set_second_place(None)
    self.set_third_place(None)
    
  def validate_podium(self, car_driver):
    if (self.get_first_place() == None):
      self.set_first_place(car_driver['driver'])
      car_driver['games_won'] += 1
    elif (self.get_second_place() == None and self.get_first_place() != car_driver['driver']):
      self.set_second_place(car_driver['driver'])
    elif (self.get_third_place() == None and self.get_first_place() != car_driver['driver'] and self.get_second_place() != car_driver['driver']):
      self.set_third_place(car_driver['driver'])
  
  def print_podium(self):
    print('\n ----|Podio|----')
    print(f"1. Primer Lugar: {self.get_first_place()}")
    print(f"2. Segundo Lugar: {self.get_second_place()}")
    print(f"3. Tercer Lugar: {self.get_third_place()}")
    
  def is_podium_completed(self):
    return self.get_first_place() != None and self.get_second_place() != None and self.get_third_place() != None
  
  def assing_podium_list(self, podium_list):
    podium_list.append({
      'first': self.get_first_place(),
      'second': self.get_second_place(),
      'third': self.get_third_place(),
    })
    return podium_list