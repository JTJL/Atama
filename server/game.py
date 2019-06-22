import socket
import random
import json
import collections
import config
from round import Round

class Game:
  def __init__(self, ip, port):
    self.s = socket.socket()
    self.s.bind((ip, port))
    self.s.listen(3)
    self.client = []
    while len(self.client) < config.number_of_players:
      conn, addr = self.s.accept()
      if conn != None:
        self.log("one client joined")
      self.client.append(conn)
    for i in range(20):
      x = random.randint(0, config.number_of_players - 1)
      y = random.randint(0, config.number_of_players - 1)
      if x != y:
        self.client[x], self.client[y] = self.client[y], self.client[x]
    # TODO: finish init process
    self.score = [config.score for i in range(config.number_of_players)]
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
    self.log("close socket")
    self.s.close()