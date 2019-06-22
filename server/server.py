#!/user/bin/env python3
#-*- coding:utf-8 -*-

from game import Game
import config

if __name__ == '__main__':
  game = Game(config.ip, config.port)
  try:
    game.work()
  except:
    pass
  finally:
    game.clean()