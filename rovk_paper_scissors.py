import random
player1 = input("Select Rock, Paper, or Scissor : ").lower()
player2 = random.choice(["Rock", " Paper", "Scissor"]).lower()
print("player 2 selected:" ,player2)

if player1 == "Rock" and player2 == "Paper":
    print("player2 won")
elif player1 == "Paper" and player2 == "Scissor" :
    print("Player 2 won")
elif player1 == "Scissor" and player2 == "Rock":
    print("player 2 won")
    print("Tie")
else :
    print("player 1 won")
