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

class Game():
	def number_of_players(self):
		try:
			no_of_players = int(raw_input("How many players would you like?"))
		except NameError and ValueError:
			return self.number_of_players()
		if no_of_players>0:	
			return no_of_players	
		else:
			self.number_of_players()	

	def create_players(self, no_of_players, deck):
		players=[]
		for player in range(0, no_of_players):
			players.append(Player(deck))
		dealer = self.create_dealer(deck)	
		return players, dealer

	def create_dealer(self, deck):
		return Dealer(deck)		
		

if __name__ == "__main__":
	# Create a deck instance
	deck = Deck()
	
	# Create an ordered deck using Deck() instance
	ordered_deck = deck.add_deck()

	#Shuffle the ordered deck to represent real life
	shuffled_deck = deck.shuffle_deck(ordered_deck)

	#Create a new game instance
	game = Game()

	#Request the number of players for the game
	no_of_players = game.number_of_players()

	#Add instances of those players as Players(), 
	#create the dealer & 
	#give them all the deck to use
	players, dealer = game.create_players(no_of_players, shuffled_deck)

	#Get a card for each player in the game and print
	for i in range(0, len(players)):
		print players[i].get_card()
	print dealer.get_card()	
	# for i in range(0, 13):
	# 	print dealer.get_card()
	# 	print player.get_card()

	# print shuffled_deck