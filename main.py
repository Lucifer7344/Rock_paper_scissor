"""
workflow:
1. user input(rock, paper, scissor)
2. computer choice(computer choose randomly)
3. result print
 case:

   A-Rock

rock vs rock = draw
rock vs paper = paper wins
rock vs scissor = rock wins

   B-Paper 

paper vs rock = paper wins
paper vs paper = draw
paper vs scissor = scissor wins

   C-Scissor

scissor vs rock = rock wins
scissor vs paper = scissor wins
scissor vs scissor = draw

"""
import random
user = input("Enter your choice: rock, paper, scissor:-\n")
computer_choice=['rock', 'paper', 'scissor']
computer = random.choice(computer_choice) 
print(f"user choice: {user}, computer: {computer}")

if user == computer:
    print("Both choices same match  draw")
elif user == 'rock':
   if computer == 'paper':
       print("rock covers paper: computer wins")
   else:
      print("Rock smashes scissor: you wins")
elif user == 'paper':
   if computer == 'rock':
       print("rock covers paper: you wins")
   else:
      print("Scissor cuts paper: computer wins")
elif user == 'scissor':
   if computer == 'rock':
       print("Rock broke scissor: computer wins")
   else:
      print("Scissor cuts paper: you wins")