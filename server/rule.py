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
    return ret

  def __int__(self):
    return color * 36 + (num - 1) * 4 + index

class Fuuro:
  def __init__(self,_cards):
    self.cards = cards
    
class Cards:
  def __init__(self, _handcards, _fuuros):
    self.handcards = _handcards
    self.fuuros = _fuuros