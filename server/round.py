import socket
import random
import json
import collections
import config
from player_agent import Player, AIPlayer, ClientPlayer

class Round:
  def __init__(self, clients, dealer):
    self.players = []
    for client in clients:
      self.players.append(ClientPlayer(client))
    while len(self.players) < config.number_of_players:
      self.players.append(AIPlayer("easy"))

  def __enter__(self):
    pass

  def __exit__(self, exc_type, exc_value, traceback):
    pass

  def get_round_start_info(self):
    pass

  def generate_round(self):
    self.yama = collections.deque()
    # TODO: generate yama

  def work(self):
    self.generate_round()

    pass


    