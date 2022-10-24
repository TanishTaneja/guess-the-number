from art import logo
import random
sec_num=random.randint(1,100)
print(logo)
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

