#!/user/bin/env python3
#-*- coding:utf-8 -*-

import socket
import random
import json
import collections

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

class Round:
  def __init__(self, clients, dealer):
    self.players = []
    for client in clients:
      self.players.append(ClientPlayer(client))
    while len(self.players) < 3:
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

class Game:
  def __init__(self, ip, port):
    self.s = socket.socket()
    self.s.bind((ip, port))
    self.s.listen(3)
    self.client = []
    while len(self.client) < 3:
      conn, addr = self.s.accept()
      if conn != None:
        self.log("one client joined")
      self.client.append(conn)
    for i in range(20):
      x = random.randint(0, 2)
      y = random.randint(0, 2)
      if x != y:
        self.client[x], self.client[y] = self.client[y], self.client[x]
    # TODO: finish init process
    self.score = [35000, 35000, 35000]
    self.point_stick_pool = 0
    self.dealer = 0

  def log(self, info):
    print("Log :", info)

  def work(self):
    # TODO: change one round to multiround
    with Round(self.client, self.dealer) as round:
      result = round.work()
    # TODO: deal with result

  def clean(self):
    self.s.close()

if __name__ == '__main__':
  game = Game('127.0.0.1', 55522)
  game.work()
  game.clean()