# do you want to play a game y/n
# deal for cards
# user gets 2 cards (removing them from a deck)
# dealer (computer) gets 2 cards (removing them from the deck)
# show 2 user cards 
# show 1 dealer card
# user enters y/n to hit
# if user > 21 then bust
# dealer draws if <16 (loop until > 16 or busted)
# print winner

import random # forrandom choices

# function to create deck as list

def create_deck():
	deck =[]
	for num in range(1,12):
		for suit in ('C','D','H',"S"):
			card = (num,suit)
			deck.append(card)
	return deck
		
# initial deal
def deal(deck):
	card = random.choice(deck)
	deck.remove(card)
	return card,deck

# function for checking score
def check_score(cards):
	score = 0
	for i in range (len(cards)):
		score += (cards[i][0])
	return score

# show scores
def show_scores(user_cards,dealer_cards):
	print(" ")
	print(f'User holds {user_cards} and scores {check_score(user_cards)}')
	print(f'Dealer holds {dealer_cards} and scores {check_score(dealer_cards)}')
	print(" ")
	return

# Ask user for game

# Main

deck = create_deck()


# empty hands
user_cards = []
user_score = 0
dealer_cards =[]

user_move = 'h'

# deal cards and
# remove card from deck

card, deck = deal(deck)
user_cards.append(card)
card, deck = deal(deck)
dealer_cards.append(card)
card, deck = deal(deck)
user_cards.append(card)

show_scores(user_cards,dealer_cards)

while user_move =='h':
	user_move = input('Hit or Stick (h/s) :').lower()
	if user_move == 'h':
		card, deck = deal(deck)
		user_cards.append(card)
		show_scores(user_cards,dealer_cards)
	if check_score(user_cards) >21:
		print ("Over 21 - You lose")
		break
	elif user_move =='s':
		card, deck = deal(deck)
		dealer_cards.append(card)
		show_scores(user_cards,dealer_cards)
		if check_score(dealer_cards) <=16:
			card, deck = deal(deck)
			dealer_cards.append(card)
			show_scores(user_cards,dealer_cards)
		if check_score(dealer_cards) >=16 and check_score(dealer_cards)<21 and check_score(user_cards)< check_score(dealer_cards):
			show_scores(user_cards,dealer_cards)
			print("Dealer wins!")
			break
		if check_score(dealer_cards) >21:
			print ("Dealer over 21 - You win")
			break
		
print("GAME OVER!")
		
	
