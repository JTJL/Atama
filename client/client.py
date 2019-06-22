#!/user/bin/env python3
#-*- coding:utf-8 -*-

import socket
import random
import json
import collections

class Game:
  def __init__(self, ip, port):
    self.s = socket.socket()
    self.s.connect((ip, port))

  def log(self, info):
    print("Log :", info)

  def work(self):
    while True:
      res = self.s.recv(1024)
      if res != '':
        self.log(res)

  def clean(self):
    self.s.close()

if __name__ == '__main__':
  game = Game('127.0.0.1', 55522)
  try:
    game.work()
  except:
    pass
  finally:
    game.clean()