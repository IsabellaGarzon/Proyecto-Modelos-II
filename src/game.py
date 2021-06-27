import shortuuid
import random
import json
import os

from src.player import Player
from src.car import Car
from src.driver import Driver
from src.track import Track
from src.trail import Trail

class Game:
  def __init__(self, game_id):
    self.id = game_id
    self.is_running = True
    print(f'Juego con ID: {game_id} \n')
  
  def get_id(self):
    return self.id
  
  def set_is_running(self, is_running):
    self.is_running = is_running
  
  def get_is_running(self):
    return self.is_running
  
  def set_players(self, players):
    self.players = players
    
  def get_players(self):
    return self.players
  
  def ask_for_players(self):
    players_number = 0
    while(players_number < 3):
      players_number = int(input('¿Cuántos jugadores desea crear? (Mínimo 3): '))
    return players_number
    
  def generate_players(self, players_number):
    players = {}
    for i in range(players_number):
      players = self.player_setup(players, (i+1))
    return players
  
  def player_setup(self, players, position):
    name = input(f'Ingrese el nombre del jugador # {(position)}: ')
    player = Player(shortuuid.uuid(), name)
    players[player.get_id()] = player.get_name()
    return players
  
  def create_track(self, players_number):
    track_size = int(input('¿Cuántos kilómetros desea recorrer en la pista? '))
    track = Track(shortuuid.uuid(), track_size, players_number)
    return track
  
  def generate_car_drivers(self, track, players):
    car_drivers = []
    for i, player in enumerate(players.items()):
      car = Car(shortuuid.uuid(), (i+1))
      driver = Driver(player[1], car.get_number())
      trail = Trail(track.kilometers, (i+1))
      car_drivers.append({
        'driver': driver.get_driver(), 'traveled_distance': 0,
        'car_id' : car.get_id(),
        'car_number' : car.get_number(),
        'trail_size' : trail.get_meters(),
        'trail_number': trail.get_number(),
        'track_id' : track.get_track_id(),
        'games_won': 0,
      })
    return car_drivers
  
  def throw_dice(self):
    return (random.randint(1, 6) * 100)
  
  def print_track_field(self, car_driver):
    print(f" {car_driver['traveled_distance']} mts ----------------------- {car_driver['trail_size']} mts")
    print(f" {car_driver['driver']} - Carro:{car_driver['car_number']}")
    print(f" --------- Carril - {car_driver['trail_number']} ---------------")
  
  def move_car(self, car_driver):
    dice_value = self.throw_dice()
    new_distance = car_driver['traveled_distance'] + dice_value
    if new_distance <= car_driver['trail_size']: 
      car_driver['traveled_distance'] = new_distance
  
  def save_game_to_json(self, game_id, data):
    self.validate_json_file()
    self.overwrite_json_file(game_id, data)
      
  def validate_json_file(self):
    if not os.path.isfile('car-console-games.json'):
      with open('car-console-games.json', 'w', encoding='utf-8') as new_file:
        json.dump({}, new_file, ensure_ascii=False, indent=2)
      new_file.close()
  
  def overwrite_json_file(self, game_id, data):
    read_file = open('car-console-games.json', 'r')  
    json_object = json.load(read_file)
    read_file.close()
    json_object[game_id] = data
    with open('car-console-games.json', 'w', encoding='utf-8') as file:
      json.dump(json_object, file, ensure_ascii=False, indent=2)
      
  def clean_traveled_distances(self, car_drivers):
    for car_driver in car_drivers:
      car_driver['traveled_distance'] = 0
  
  def validate_yes_response(self, podium, car_drivers):
    podium.clean_podium()
    self.clean_traveled_distances(car_drivers)
  
  def validate_no_response(self, podium_list, car_drivers):
    game_id = f'game_{self.get_id()}'
    data = {
      'podium': podium_list,
      'game_data': car_drivers
    }
    self.save_game_to_json(game_id, data)
    self.set_is_running(False)
    