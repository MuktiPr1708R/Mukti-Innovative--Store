
from itertools import repeat
import random as rd
rand_No = rd.randint(1,3)
print(str(rand_No))
if rand_No == 1:
     a = "s"
elif rand_No == 2:
     a = "p"
elif rand_No == 3:
     a = "sc"

def game(a,b):
     if a == b:
          return None
     elif a=="s":
          if b == "p":
               return True
          elif b == "sc":
               return False
     elif a=="p":
          if b == "sc":
               return True
          elif b == "s":
               return False
     elif a=="sc":
          if b == "s":
               return True
          elif b == "p":
               return False




print("Computer's turn: stone(s), paper (p) , scissor (sc) ")
print("your turn: stone(s), paper (p) , scissor (sc) ")
b = input("your turn: stone(s), paper (p) , scissor (sc) : " )
print(f"computer chose {a}")
game_win = game(a,b)
if game_win == None:
     print("Game tie!  play again")
     # repeat(game(a,b))
elif game_win == True :
     print("\b YOU WON")
else:
     print("you lose")