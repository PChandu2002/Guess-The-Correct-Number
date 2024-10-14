import random

target = random.randint(1,100)
print("Welcome to the guessing game! Try to guess the number between 1 and 100.")
while True:
    try:
        x = input("Enter the guess number or Quit (Q): ")
        if (x == "Q"):
            break
        x = int(x)
        if (x == target):
            print("you guess the correct number : ",x)
            break
        elif( x < target):
            print("your guess is too small.guess bigger number")
        else:
            print("your guess is too big .guess smaller number")
            
    except:
        print("Invalid input! Please enter a valid integer.")

print("........game is over.......")