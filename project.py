import random
import time

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


#Write your code below this line 👇
def play():
    numRand = random.randint(0, 2)
    map = [rock, paper, scissors]
    numi = input(
        "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: \n"
    )
    num = int(numi)
    if numRand == 0 and num == 0:
        print(map[num])
        print("Computer chose:\n")
        print(map[numRand])
        print("It's a draw")
    elif numRand == 0 and num == 1:
        print(map[num])
        print("Computer chose:\n")
        print(map[numRand])
        print("Your win!")
    elif numRand == 0 and num == 2:
        print(map[num])
        print("Computer chose:\n")
        print(map[numRand])
        print("You lose!")
    elif numRand == 1 and num == 0:
        print(map[num])
        print("Computer chose:\n")
        print(map[numRand])
        print("You lose!")
    elif numRand == 1 and num == 1:
        print(map[num])
        print("Computer chose:\n")
        print(map[numRand])
        print("It's a draw")
    elif numRand == 1 and num == 2:
        print(map[num])
        print("Computer chose:\n")
        print(map[numRand])
        print("Your win!")
    elif numRand == 2 and num == 0:
        print(map[num])
        print("Computer chose:\n")
        print(map[numRand])
        print("Your win!")
    elif numRand == 2 and num == 1:
        print("You lose!")
    elif numRand == 2 and num == 2:
        print(map[num])
        print("Computer chose:\n")
        print(map[numRand])
        print("It's a draw")


while True:
    play()
    time.sleep(1)
    ask = input("Do you want to keep playing? y|n\n")
    if ask == "y":
        play()
        time.sleep(1)
    else:
        break
