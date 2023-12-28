print("Welcome to auction program\n")
bid_dict = {}

def details(bidders_name,bid_amount,i):
  dict = {}
  dict["bidders_name"] = bidders_name
  dict["bid_amount"] = bid_amount
  bid_dict[i] = dict
  
i = 1
process = True

while process:
  name = input("What is your name?\n")
  bid = int(input("What is your amount?\n"))
  details(name,bid,i)
  choice = input("Are there any other bidders?Yes or No?\n").lower()
  if choice == "yes":
    i = i+1
  else:
    max = 0
    person = ""
    for item in bid_dict:
      if bid_dict[item]["bid_amount"]>max:
        max = bid_dict[item]["bid_amount"]
        person = bid_dict[item]["bidders_name"]
    print(f"The winner of the bid is {person} with bid ${max}\n")
    process = False
