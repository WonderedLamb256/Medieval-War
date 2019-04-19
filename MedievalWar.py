import time
import MedievalWars
print("Medieval Wars: text adventure by WonderedLamb256")
time.sleep(1)
name = str(input("Input the player\'s name...\n"))
time.sleep(3)
print("Loading classes and modules...")
import random
health1 = 100
attack1 = random.randint(25, 50)
poisoned = False
poisontimer = 4
criticaldmg = 0
totalatk = 0
inatk = False
# Classes
class Player:
	if health1 == 0:
		print("You lost!")
	while poisoned == True:
		health1 = health1 - 3
		time.sleep(1.5)
		poisontimer = poisontimer - 1
	if poisontimer == 0:
		poisoned = False
		poisontimer = 4
# Player attack function
def atk(n):
	if n == 1:
		print(name, "attacked!")
		criticaldmg = random.randint(0, 5)
		attack1 = random.randint(25, 50)
		totalatk = attack1 + criticaldmg
		tuple = ('totalatk')
		attack1, criticaldmg, totalatk = random.randint(25, 50), random.randint(0, 5), 0
	elif n == 2:
		print("Feature implemented soon...")
	elif n == 3:
		print(name, "ran away!")
		health1 = health1 - 10
		inatk = False
	else:
		print("Please choose again.")
# Monster types
monsteratk = 0
canpoison = False
mdead = False
health2 = 0
mname = str("LoremIpsum")
class Monster:
	health2 = random.randint(10, 100)
	if health2 < 26:
		mname = str("Ogre")
		monsteratk = 25
		canpoison = False
	elif health2 < 51:
		mname = str("Knight")
		monsteratk = 35
		canpoison = False
	elif health2 > 50:
		mname = str("Alchemist")
		monsteratk = random.randint(35, 50)
		canpoison = True
# Monster attacked detector
mloop2 = True
if mloop2 == True:
	for t	in tuple:
		if len(tuple) == 3:
			print(mname, "took", tuple, "damage!")
# Loading stops here
def debug():
	print(health2)
print("Loading finished!")
time.sleep(5)
MedievalWars.Player
MedievalWars.atk
MedievalWars.debug
mloop = True
# Monster attacked message
if monstersignal == True:
	print(mname, "\'s health is now", health2)
# Monster death checker
if mloop == True:
	if health2 == 0:
		print(mname, "has died!")
		mdead = True
		health2 = random.randint(10, 100)
	MedievalWars.Monster
	print("You encountered a", mname, "!")
	inatk = True
	# Monster poison checker
if mloop == True:
	if canpoison == True:
		poisonchance = random.randint(1, 5)
		if poisonchance == 3:
			poisoned = True
			time.sleep(5)
			poisonchance = random.randint(1, 5)
