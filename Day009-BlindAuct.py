
# make empty Dict
bids = {}
# Set while loop end condition
biding_ended = False

#find highest bidder
def find_high_bid(bids):
  highest_bid = 0
  winner = ""
  for bidder in bids:
    bid_amount = bids[bidder]
    if bid_amount > highest_bid: 
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")

while not biding_ended:
  name = input("What is your name?: ")
  bid_amt = int(input("What is your bid?: "))
  bids[name] = bid_amt
  anymore_bids = input("Are there any other bidders? Type 'y or 'n'.\n").lower()
  if anymore_bids == "n":
    biding_ended = True
    find_high_bid(bids)
  elif anymore_bids == "yes":
    clear() # clears the screen for the next bidder
  
