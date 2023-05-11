import time
import random
import os


def g(rolls):
	data = "qwertyuioplkjhgfdsazxcvbnm1234567890QWERTYUIOPLKJHGFDSAZXCVBNM"
	result = ""
	while rolls >= 1:
		c = random.choice(data)
		result = c + result
		rolls = rolls - 1
	return result


print("")
print("What Giftcard you need to generate?")

tt = input("\nAmazon\nRoblox\nWebkinz\nFortnite\nIMVU\nEbay\nNetflix\niTunes\nPaypal\nVisa\nPokemonTGC\nPlaystation\nSteam\nXbox\nPlayStore\nMinecraft\n\n>")

t = tt.lower()
print("")
print("How many of them?")
nn = input(">")
print("")
n = int(nn)

if t == "minecraft":
	for _ in range(n):
		print("")
		print(f"{g(4)}-{g(4)}-{g(4)}")

if t == "paypal":
	for _ in range(n):
		print("")
		print(f"{g(4)}-{g(4)}-{g(4)}")

if t == "playstation":
	for _ in range(n):
		print("")
		print(f"{g(4)}-{g(4)}-{g(4)}")

if t == "amazon":
	for _ in range(n):
		print("")
		print(f"{g(4)}-{g(6)}-{g(4)}")

if t == "netflix":
	for _ in range(n):
		print("")
		print(f"{g(4)}-{g(6)}-{g(4)}")

if t == "steam":
	for _ in range(n):
		print("")
		print(f"{g(4)}-{g(6)}-{g(5)}")

if t == "fortnite":
	for _ in range(n):
		print("")
		print(f"{g(5)}-{g(4)}-{g(4)}")

if t == "robolox":
	for _ in range(n):
		print("")
		print(f"{g(3)}-{g(3)}-{g(4)}")

if t == "itunes":
	for _ in range(n):
		print("")
		print(g(16))

if t == "ebay":
	for _ in range(n):
		print("")
		print(g(10))

if t == "imvu":
	for _ in range(n):
		print("")
		print(g(10))

if t == "webkinz":
	for _ in range(n):
		print("")
		print(g(8))

if t == "pokemontgc":
	for _ in range(n):
		print("")
		print(f"{g(3)}-{g(4)}-{g(3)}-{g(3)}")

if t == "playstore":
	for _ in range(n):
		print("")
		print(f"{g(4)}-{g(4)}-{g(4)}-{g(4)}-{g(4)}")

if t == "xbox":
	for _ in range(n):
		print("")
		print(f"{g(5)}-{g(5)}-{g(5)}-{g(5)}-{g(5)}")

print("")
print("-----Generation completed-----")
print("PRess any key to exit")
input = input(">")
os.system("python main.py")