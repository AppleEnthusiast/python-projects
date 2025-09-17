import random

suits = ["Hearts","Diamonds","Spades","Clubs"]
ranks = ["Ace",2,3,4,5,6,7,8,9,10,"Jack","Queen","King"]

deck = [f"{rank} of {suit}" for suit in suits for rank in ranks]

print(deck[:5])

random.shuffle(deck)
print(deck[:5])

drawn_card = random.choice(deck)
print()
print(f"Drawn card: {drawn_card}")

