### 2nd Milestone Project ###
# Import files
import random

suits = {'Diamond','Club','Heart','Spade'}
ranks = {'Two','Three','Four','Five','Six','Seven','Eight','Nine','Jack','Queen','King','Ace'}
values = {'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Jack':10,'Queen':10,'King':10,'Ace':11}

playing = True

# Define class

class Card:

	def __init__(self,suits,cards):
		self.suit = suits
		self.rank = ranks

	def __str__(self):
		return self.rank + 'of' + self.suit

class Deck:

	def __init__(self):
		self.deck = []
		for suit in suits:
			for rank in ranks:
				self.deck.append(Card(suit,rank))

	def __str__(self):
		deck_comp = ''
		for card in self.deck:
			deck_comp += '\n'+card.__str__()
		return 'The deck has: ' + deck_comp

	def shuffle(self):
		random.shuffle(self.deck)

	def deal(self):
		single_card = self.deck.pop()
		return single_card

class Hand:

	def __init__(self):
		self.cards = []
		self.value = 0
		self.aces = 0

	def add_card(self,card):
		self.card.append(card)
		self.value += value[card.rank]
		if card.rank == 'Ace':
			self.aces += 1

	def adjust_for_ace(self):
		while self.value > 21 and self.aces:
			self.value -= 10
			self.aces -= 1

class Chips:
	
	def __init__(self):
		self.total = 100
		self.bet = 0

	def win_bet(self):
		self.total += self.bet

	def lose_bet(self):
		self.total -= self.bet

# Define functions

def take_bet(chips):

	while True:
		try: 
			chips.bet = int(input('How many chips would you like to bet?'))
		except ValueError:
			print('Sorry, a bet must be a number from 0 to ',chips.total)
		else:
			if chips.bet > chips.total:
				print("Sorry, your bet can't exceed ",chips.total)
			else:
				break

def hit(deck,hand):
	hand.add_card(deck.deal())
	hand.adjust_for_ace()

def hit_or_stand(deck,hand):
	global playing

	while True:
		x = input("Would you like to Hit or Stand? Input 'h' or 's'")

		if x[0].lower() == 'h':
			hit(deck,hand)

		elif x[0].lower() == 's':
			print("Player stands. Dealer is playing.")
			playing = False

		else:
			print("Sorry, please try again")
			continue
		break

def show_some(player,dealer):
	print("Dealer's Hand:")
	print(" <Card Hidden> ")
	print('',dealer.cards[1])
	print("\nPlayer's Hand:", *player.cards, sep='\n')


def show_all(player,dealer):
	print("\nDealer's Hand: ", *dealer.cards, sep='\n')
	print("Dealer's Hand = ", dealer.value)
	print("\nPlayer's Hand: ", *player.cards, sep='\n')
	print("Player's Hand = ", player.value)

def player_bust(player,dealer,chips):
	print("Player Busts!")
	chips.lose_bet()

def player_wins(player,dealer,chips):
	print("Player Wins!")
	chips.win_bet()

def dealer_busts(player,dealer,chips):
	print("Dealer Busts!")
	chips.win_bet()

def dealer_wins(player,dealer,chips):
	print("Dealer Wins!")
	chips.lose_bet()

def push(player,dealer):
	print("Tie game!")

# Gameplay

while True:
	print('Welcome to BlackJack!')

	#create and shuffle deck & deal 2 cards each player
	deck = Deck()
	deck.shuffle()

	player.hand = Hand()
	player.hand.add_card(deck.deal())
	player.hand.add_card(deck.deal())

	dealer.hand = Hand()
	dealer.hand.add_card(deck.deal())
	dealer.hand.add_card(deck.deal())

	#setup player chips
	player_chips = Chips()

	#prompt player for bet
	take_bet(player_chips)

	#show cards
	show_some(player_hand,dealer_hand)

	#player choose whether to hit or stop

	while playing:

		hit_or_stand(deck,player_hand)
		show_some(player_hand,dealer_hand)

		if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_chips)
            break

    if player_hand.value <= 21:

    	while dealer_hand.value <17:
    		hit(deck,dealer_hand)

    	show_all(player_hand,dealer_hand)

    	if dealer_hand.value > 21:
    		dealer_busts(player_hand,dealer_hand,player_chips)

    	elif dealer_hand.value > player_hand.value:
    		dealer_wins(player_hand,dealer_hand,player_chips)

    	elif dealer_hand.value < player_hand.value:
    		dealer_wins(player_hand,dealer_hand,player_chips)

    	else:
    		push(player_hand,dealer_hand)

    print("\nPlayer's winnings stand at ", player_chips.total)

    new_game = input("Would you like to play again? Y or N")
    if new_game[0].lower() == 'y':
    	playing = True
    	continue
    else:
    	print("Thanks for playing!")
    	break

