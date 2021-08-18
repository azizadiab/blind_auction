from art import logo

bid = {}
def add_dict(name,value):#function to add the name and bid value to the bid dictionary
  if name in bid.keys():
    print("Name already existed. Entry not added. ")
  else:
    bid[name] = value

def max_bid(bid_dict):#To find out ht emax value in the bid dicttionary
  max1 = 0
  name = ""
  for key,value in bid.items():
    if max1 < int(value):
      max1 = value
      name = key
  return max1,name

print(logo)
continue_bid = True

while continue_bid:#program will run as long as the user input "no"
  bidder_name = input("What is your name? ")
  bid_value = int(input("What is your bid? "))
  add_dict(bidder_name, bid_value)
  yes_no = input("Are there any other bidders (yes/no)?".lower())
  if yes_no == "no":
    continue_bid = False

max_value,max_name = max_bid(bid)
print(f"The winner is {max_name} with a bid of ${max_value}.")