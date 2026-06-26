import random
print("welcome to the number guessing game")
def number_guess() :
    computer_number = random.randint(1, 100)
    print(computer_number)
    
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == "easy" :
        attempts = 10
        print(f"You have {attempts} attempts remaining to guess the number.")
        user_guess = int(input("Make a guess: "))
        if user_guess == computer_number :
            print(f"You got it! The answer was {computer_number}.")
        else :
            
            
            print(f"since u guess one already so you have {attempts} attempts remaining to guess the number.")
            while attempts > 1 :
                
                if user_guess >computer_number :
                    attempts -= 1
                    print("Too high.")
                    print("Guess again.")
                    print(f"You have {attempts} attempts remaining to guess the number.")
                    user_guess = int(input("Make a guess: "))

                if user_guess == computer_number :
                    print(f"You got it! The answer was {computer_number}.")
                    break

                if user_guess < computer_number :
                    attempts -= 1
                    print("Too low.")
                    print("Guess again.")
                    print(f"You have {attempts} attempts remaining to guess the number.")
                    user_guess = int(input("Make a guess: "))

            if attempts == 1 :
                print (f"You've run out of guesses, you lose. The number was {computer_number}.")
    elif difficulty == "hard" :
        attempts = 5 
        print(f"You have {attempts} attempts remaining to guess the number.")
        user_guess = int(input("Make a guess: "))
        if user_guess == computer_number :
            print(f"You got it! The answer was {computer_number}.")
        else :
            while attempts > 1 :
                
                if user_guess >computer_number :
                    attempts -= 1
                    print("Too high.")
                    print("Guess again.")
                    print(f"You have {attempts} attempts remaining to guess the number.")
                    user_guess = int(input("Make a guess: "))
                
                if user_guess == computer_number :
                    print(f"You got it! The answer was {computer_number}.")
                    break

                if user_guess < computer_number :
                    attempts -= 1
                    print("Too low.")
                    print("Guess again.")
                    print(f"You have {attempts} attempts remaining to guess the number.")
                    user_guess = int(input("Make a guess: "))

            if attempts == 1 :
                print (f"You've run out of guesses, you lose. The number was {computer_number}.")
number_guess()
        