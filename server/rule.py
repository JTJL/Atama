def sgn(x):
  if (x < 0):
    return -1
  if (x > 0):
    return 1
  return 0

'''
int color: 0 for m, 1 for s, 2 for p, 3 for z 
int num: [1-9] for m,s,p  [1-7] for z 
int index [0-3]
'''

class Card:
  def __init__(self, _color, _num = -1, _index = -1):
    if (_num == -1):
      V = _color
      _color = V // (9 * 4)
      _num = (V % (9 * 4)) // 4 + 1
      _index = V % 4
    self.color = _color
    self.num = _num
    self.index = _index
    #card.value = (_color, _num, _index)

  def __str__(self):
    if (self.color == 3):
      return ["ton","nan","shi","pei","haku","hatsu","chou"][self.num - 1]
    ret = str(self.num) + "mspz"[self.color]
    if (self.num == 5 and self.index == 0):
      ret += '_red'
    return 
    
  def __cmp__(self, other):
    ret = (self.color - other.color, self.num - other.num, self.index - other.index)
    for i in range(3):
      if (ret[i] != 0):
        return sgn(ret[i])
    return 0

  def __eq__(self,other):
    return (self.__cmp__(other) == 0)

  def __int__(self):
    return color * 36 + (num - 1) * 4 + index

'''
describe a fuuro
type in {'chi', 'pon', 'kan', 'ankan'}
use a set of Card to store the cards
triiger card and trigger player describe the event triggers the fuuro
'''
class Fuuro:
  def __init__(self,_cards,_type,_trigger_card,_trigger_player):
    self.cards = _cards
    self.type = _type
    self.trigger_card = _trigger_card
    self.trigger_player = _trigger_player
    
'''
describe all the cards of a player

'''
class Cards:
  def __init__(self, _handcards, _fuuros):
    self.handcards = _handcards
    self.fuuros = _fuuros