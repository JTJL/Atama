import socket
import random
import json
import collections
import config

class Player:
  def __init__(self):
    self.kawa = []
    self.leftkawa = []
    self.rightkawa = []
    self.fuuro = []
    self.leftfuuro = []
    self.rightfuuro = []
    self.dora = []

class AIPlayer(Player):
  def __init__(self, type):
    pass

class ClientPlayer(Player):
  def __init__(self, client):
    self.client = client

  def send_info(self, info):
    # send json format info
    self.client.send(bytes(json.dumps(info) + '\n', encoding = 'utf-8'))

  def recv_info(self):
    pass
    return "www"