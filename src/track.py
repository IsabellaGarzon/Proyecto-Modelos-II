class Track:
  def __init__(self, track_id, kilometers, trails):
    self.track_id = track_id
    self.kilometers = kilometers
    self.trails = trails
    
  def get_track_id(self):
    return self.track_id
  
  def get_kilometers(self):
    return self.kilometers
  
  def get_trails(self):
    return self.trails