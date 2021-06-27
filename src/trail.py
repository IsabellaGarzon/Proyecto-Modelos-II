class Trail:
  def __init__(self, kilometers, trail_number):
    self.meters = kilometers * 1000
    self.trail_number = trail_number
    
  def get_meters(self):
    return self.meters
  def get_number(self):
    return self.trail_number