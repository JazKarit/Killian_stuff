import random

def randompowE(level):
	enemypow = level*(int(random.randint(1,100)) / 100)
	return enemypow

lv_up = 0
lv_boostmult = 0
lv_up_curvemult = 5

hero_info = {
	'hp':50,
	'def':5,
	'atk':5,
	'lv':1 + int(lv_up), 
	'xp':0
	}
mage_info = {
	'hp':35,
	'def':3,
	'atk':3
	}
paladin_info = {
	'hp':45,
	'def':7,
	'atk':8
	}
print(hero_info['hp'])
