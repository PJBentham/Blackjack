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
		self.score = 0

	def get_card(self):
		while len(self.deck)>0:
			hand = self.deck.pop(0)
			return self.cards.append(hand)
		else:
			return "Sorry no more cards remain in the pack!"

	##############################################################
	def get_cards_score(self, player_number="[Dealer]", isdealer=False):
		values = {
		'Ace': 11,
		'King': 10,
		'Queen': 10,
		'Jack': 10,
		}
		card_values = 0

		for card in range(0, len(self.cards)):
			if isinstance(self.cards[card][1], int): 
				card_values += self.cards[card][1]
			elif self.cards[card][1] == 'Ace':
				if isdealer == True:
					card_values = "1 or 11"
				else:	
					print 'Player {}, your cards are: {}'.format(player_number, self.cards)
					valid_answer = False
					while valid_answer == False:
						high_or_low = raw_input('Do you want your Ace to be high[h] or low[l]?').lower()
						if high_or_low == 'h':
							card_values += 11
							valid_answer = True
						elif high_or_low == 'l':
							card_values += 1
							valid_answer = True

			else:	
 				card_values += values[self.cards[card][1]]		
		self.score = card_values
		return self.score
	###################################################################		

	def stick_or_twist(self):
		valid_answer = False
		while valid_answer == False:
			choice = raw_input("Do you want to stick[s] or twist[t]?").lower() 		
			if choice == 's':
				print "You are sticking with a score of {}".format(self.score)
				valid_answer = True
			elif choice	== 't':
				print "You have decided to twist."
				valid_answer = True
				self.get_card()
				print "Your next card is: "+str(self.cards[-1])
				self.get_cards_score()
				if self.score > 21:
					print "You are bust"
					break
				elif self.score == 21:
					print "You have Blackjack!"
					break
				else:
					return self.stick_or_twist()

class Dealer(Player):
	def stick_or_twist(self):
		while self.score < 17:
			print "Your score is below 17, you have to twist"
			self.get_card()
			self.get_cards_score()
			print 'Your cards are: {} and your new score is {}'.format(self.cards, self.score)

		if self.score > 21:
			print "Dealer is bust, all remaining win"
		elif self.score == 21:
			print "Dealer has Blackjack"

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

	def show_players_cards(self, players, dealer):
		for player in range(0, len(players)):
			print "Player {}'s cards: {}, Score is: {}".format(	(player+1), 
																self.get_players_cards(players[player]), 
																players[player].get_cards_score(
																	player+1))
		print "Dealers card: {}, Score is: {}".format(	self.get_players_cards(dealer),
														dealer.get_cards_score(
															isdealer=True))

	def run_stick_or_twist(self, players, dealer):
		for player in range(0, len(players)):
			print "Player {}, your cards are {}".format(player+1, players[player].cards)
			players[player].stick_or_twist()
		print "Dealer, your cards are {}".format(dealer.cards)	
		dealer.stick_or_twist()	

		
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
	
	#Ask the players if they want to stick or twist
	game.run_stick_or_twist(players, dealer)

	#print players[0].get_cards_score()
	#players[0].stick_or_twist()