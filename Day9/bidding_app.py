# TODO-1: Ask the user for input
bflag = True
bidder_info = {}



while True:
    
    user_name = input("Enter user's name: ")
    user_bid = int(input("Enter user's bid: "))
    ask_bidders = input("More bidders? Types 'yes'/'no ")
    bidder_info[user_name] = user_bid
    if ask_bidders.lower() == 'yes' or  ask_bidders.lower() ==  'y':
        continue
        
    elif ask_bidders.lower() == 'no' or  ask_bidders.lower() == 'n':
        break


print(bidder_info)

# turns values into a list when using the mrthof vslues()
values = bidder_info.values()
largest = 0

for max_bidder in values:
    if max_bidder > largest:
        largest = max_bidder
print(largest)
    



    
# TODO-4: Compare bids in dictionary


