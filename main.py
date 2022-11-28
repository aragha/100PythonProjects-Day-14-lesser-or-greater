# from game_data import data
from art import logo, vs
from replit import clear
# a. Analyzing the data
# 1. type(data) - indicates it's a list
# 2. print(data) - dumped a dictionary like structure
# 3. for i in data:
#     print(i)
# - prints a collection of dictionaries
# 4. for i in data:
#     for k in i:
#       print(k)
# -  prints a repeated collection of keys
# name
# follower_count
# description
# country
# 5. len(data) - returns 50
# 6. print(data[0]) - prints 
# {'name': 'Instagram', 'follower_count': 346, 'description': 'Social media platform', 'country': 'United States'}
# b. Write functions for the following:
#   1. getting 2 random, unequal records from data
#   2. get user's input as to which is greater
#   3. if user's choice is correct, give them victory, else loss
#   4. loop until user doesn't want to play any further

# function to return 2x different records
def find_competitors():
  from game_data import data
  import random 
  choice1 = random.randint(0, len(data)-1)
  choice2 = random.randint(0, len(data)-1)      
  while choice1 == choice2:
    choice2 = random.randint(0, len(data)-1)    
  competitor_list = []
  competitor_list.append(data[choice1])
  competitor_list.append(data[choice2])
  return(competitor_list)
  
def decide_success(cl)  :
  if cl[0]['follower_count'] > cl[1]['follower_count']:
    return 0
  else:
    return 1
game_over = False
while not game_over:
  clear()
  comp = find_competitors()
  # print(comp)
  correct_result = decide_success(comp)
  # print(correct_result)
  print(logo)
  print(f"Compare A: {comp[0]['name']}, a {comp[0]['description']}, from {comp[0]['country']}")
  print(vs)
  print(f"B: {comp[1]['name']}, a {comp[1]['description']}, from {comp[1]['country']}")
  user_choice = input("Who has more followers? Type 'A' or 'B'")
  user_choice = user_choice.upper()
  # print(user_choice)
  if user_choice == 'A' and correct_result == 0:
    print(f"You are correct! {comp[0]['name']} has {comp[0]['follower_count']} followers while {comp[1]['name']} has {comp[1]['follower_count']}")

  else:
    print(f"You are incorrect {comp[0]['name']} has {comp[0]['follower_count']} followers while {comp[1]['name']} has {comp[1]['follower_count']}")
    game_over = True
