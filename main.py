import random

options: list = ["rock", "paper", "scissor"]


def get_choices():
  player_choice: str = input("enter a choice (rock, paper or scissors) : ")
  computer_choice: str = random.choice(options)
  choices = {"player": player_choice, "computer": computer_choice}

  return choices


def check_win(player, computer):
  print(f"You chose {player}, and computer chose {computer} ")
  if player == computer:
    return "it's a tie"
  elif player == 'rock':
    if computer == 'scissor':
      return "Rock smashes scissors, You Win!"
    else:
      return "Paper covers rock, You lose"
  elif player == 'paper':
    if computer == 'rock':
      return "Paper covers rock, You Win!"
    else:
      return "scissors cuts paper, You lose"
  elif player == 'scissor':
    if computer == 'paper':
      return "scissors cuts rock, You Win!"
    else:
      return "rock smashes scissors, You lose"


choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)
