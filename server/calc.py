from rule import *
from operator import methodcaller

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

def get_all_yaku(cards):
  ret = []
  for pattern in yaku_list:
    check_ret = eval(pattern + "_checker")(cards)
    if (check_ret > 0):
      ret.append((check_ret, pattern))
  return ret

print(get_all_yaku('fuck'))