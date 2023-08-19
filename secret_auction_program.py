import clear
from art import logo

print(logo)

bid_dictionary = {}
bidding_finished = False


def finding_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


while not bidding_finished:
    name_input = input("What is your name?\n")
    bid_input = int(input("Enter your bid amount $"))

    bid_dictionary = {
        name_input: bid_input
    }
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.")
    if should_continue == "no":
        bidding_finished = True
        finding_highest_bidder(bid_dictionary)
    elif should_continue == "yes":
        clear
