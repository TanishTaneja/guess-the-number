#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

# from art import logo
import random
sec_num=random.randint(1,100)
# print(logo)
print("""Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100""")
difficulty=input("Choose a difficulty. Type 'easy' or 'hard':")

def countdown(lives):
   
    while lives!=0:
        
        print(f"You have {lives} attempts remaining to guess the number.")
        guess=int(input("Make a guess\n"))
        
        if guess==sec_num:
                print(f"You got it! The answer was {sec_num}.")
                break
        elif(guess>sec_num):
                print("Too high\nGuess again")
                lives-=1
        elif(guess<sec_num):
                print("Too low\nGuess again")
                lives-=1
        if lives==0:
            print(f"You've run out of guesses, you lose.\nThe number was {sec_num}")
            break
            
            
        
        
        


if difficulty == "hard":
    countdown(5)

elif difficulty =="easy":
    countdown(10)

else:
    print("choose easy or hard/ntry again")

