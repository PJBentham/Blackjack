from random import *

class Deck():
	def __init__(self):
		self.suits = ['Hearts', 'Clubs', 'Diamonds', 'Spades']
		self.numbers = ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King']

	def add_deck(self):
		full_deck = []
		for suit in range(0,len(self.suits)):
			for number in range(0,len(self.numbers)):
				full_deck.append((self.suits[suit],self.numbers[number]))
		return full_deck		

	def shuffle_deck(self, deck):
		shuffled_deck = deck
		shuffle(shuffled_deck)
		return shuffled_deck

class Player():
	def __init__(self, deck):
		self.deck = deck

	def get_card(self):
		while len(self.deck)>0:
			hand = self.deck.pop(0)
			return hand
		else:
			return "Sorry no more cards remain in the pack!"

class Dealer(Player):	
	pass

if __name__ == "__main__":
	deck = Deck()
	ordered_deck = deck.add_deck()
	shuffled_deck = deck.shuffle_deck(ordered_deck)

	print shuffled_deck	
	dealer = Dealer(shuffled_deck)
	player = Player(shuffled_deck)

	for i in range(0, 13):
		print dealer.get_card()
		print player.get_card()

	print shuffled_deck