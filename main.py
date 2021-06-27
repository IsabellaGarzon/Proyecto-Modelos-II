# Main Runner
import shortuuid

from src.game import Game
from src.podium import Podium

game = Game(shortuuid.uuid())
# Creating Players
players_number = game.ask_for_players()
game.set_players(game.generate_players(players_number))
# Creating the track
track = game.create_track(players_number)
car_drivers = game.generate_car_drivers(track, game.get_players())
# Racing
podium = Podium()
match_round = 0
podium_list =[]

while game.get_is_running():
  match_round+=1
  print(f' Turno #{match_round}\n')
  for car_driver in car_drivers:
    game.print_track_field(car_driver)
    if(car_driver['traveled_distance'] == car_driver['trail_size']):
      podium.validate_podium(car_driver)
    else:
      game.move_car(car_driver)
    
  if(podium.is_podium_completed()):
    podium.print_podium()
    podium_list = podium.assing_podium_list(podium_list)
    response = input('Deseas continuar jugando? (s/n)')
    if (response == 's'):
      game.validate_yes_response(podium, car_drivers)
      match_round = 0
    elif (response == 'n'):
      game.validate_no_response(podium_list, car_drivers)
