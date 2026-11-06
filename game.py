import random

def intro():
  print("Welcome to Guess My Number!\n")
  start = input("press enter to begin the game ")
  if start:
    guessGame()
  else:
    guessGame()

def guessGame():
  print("Game started!\n")
  hiddenNum = random.randint(1,100)
  attempts = []
  limit = 1
  while limit <= 8:
    try:
      userInput = int(input("Input a number: "))
    except ValueError :
      print('please enter a valid integer')
      continue
    attempts.append(userInput)
    if userInput == hiddenNum:
      print(f"Well done, it took you {len(attempts)} attempts to guess the number {userInput}")
      break
    elif userInput > 100 or userInput < 0:
      print("enter a number between 0-100!")
    elif userInput > hiddenNum:
      print(f"My number is less than {userInput}")
    elif userInput < hiddenNum:
      print(f"My number is greater than {userInput}")
    limit += 1
  else:
    print("you ran out of attempts")


intro()
