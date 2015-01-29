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
		self.cards = []

	def get_card(self):
		while len(self.deck)>0:
			hand = self.deck.pop(0)
			return self.cards.append(hand)
		else:
			return "Sorry no more cards remain in the pack!"

class Dealer(Player):	
	def show_first_card():
		return cards[0]

class Game():
	def number_of_players(self):
		try:
			no_of_players = int(raw_input("How many players would you like?"))
		except NameError and ValueError:
			return self.number_of_players()
		if no_of_players>0:	
			return no_of_players	
		else:
			return self.number_of_players()	

	def create_players(self, no_of_players, deck):
		players=[]
		for player in range(0, no_of_players):
			players.append(Player(deck))
		dealer = self.create_dealer(deck)	
		return players, dealer

	def create_dealer(self, deck):
		return Dealer(deck)	

	def deal_cards(self, players, dealer):
		dealer.get_card()
		for i in range(0, len(players)):
			players[i].get_card()
			players[i].get_card()

	def get_players_cards(self, player):
		return player.cards		
		
	def get_cards_score(self, cards):
		values = {
		'Ace': 10,
		'King': 10,
		'Queen': 10,
		'Jack': 10,
		}
		card_values = 0

		for card in range(0, len(cards)):
			#Need to put an if statement in here to see if
			#player wants to use Ace as High or Low...
			if isinstance(cards[card][1], int): 
				card_values += cards[card][1]
			else:
 				card_values += values[cards[card][1]]		
		return card_values

	def show_players_cards(self, players, dealer):
		for player in range(0, len(players)):
			print "Player {}'s cards: {}, Score is: {}".format(	(player+1), 
																self.get_players_cards(players[player]), 
																self.get_cards_score(self.get_players_cards(players[player])))
		print "Dealers card: {}, Score is: {}".format(	self.get_players_cards(dealer),
														self.get_cards_score(self.get_players_cards(dealer)))

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
	game.deal_cards(players, dealer)

	#Print players cards and dealers card
	game.show_players_cards(players, dealer)
	