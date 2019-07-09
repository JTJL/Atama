from rule import *

def chi_toi_checker(cards):
  return 0

def ko_ku_shi_checker(cards):
  return 0

def ron_dfs(handcards):
  if (len(handcards) == 0):
    return True
  return False

#no matter whether have yaku
def can_ron(cards):
  if (ron_dfs(cards.handcards)):
    return True
  return (chi_toi_checker(cards) > 0) or (ko_ku_shi_checker(cards) > 0)

def chin_i_so_checker(cards):
  ok = True
  return 1

def ri_chi_checker(cards):
  return 1

yaku_list = ["chin_i_so","ri_chi"]

'''
input: a list of several card_tuple(s)
output: a tuple (fan_sum, [(fan1, yaku1), (fan2, yaku2) ...])
'''
def get_all_yaku(cards):
  fan_sum = 0
  ret = []
  for pattern in yaku_list:
    check_ret = eval(pattern + "_checker")(cards)
    if (check_ret > 0):
      ret.append((check_ret, pattern))
      fan_sum += check_ret
  return (fan_sum, ret)

divide_ret = []

def divide_dfs(now, cards):
  if (len(cards) == 0):
    divide_ret.append(now)
    return
  
'''
input: an instance of (class Cards)
output: a list of list of several card_tuple(s)  [[ct1_1, ct1_2, ...], [ct2_1, ct2_2, ...], ...]
'''
def get_all_divides(cards):
  global now = []
  for fuuro in cards.fuuros:
    now.append(fuuro.to_card_tuple)
  divide_dfs(now, cards.handcards)

print(get_all_yaku('fuck'))