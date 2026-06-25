import random

def game():
    user_card = []
    computer_card = []
    user_cards = random.randint(0, 12), random.randint(0, 12)
    user_card += user_cards
    user_score = sum(user_card)
    computer_cards = random.randint(0, 12), random.randint(0, 12)
    computer_card += computer_cards
    computer_score = sum(computer_card)

    if user_score > 21:
        print("You went over. You lose!")
        return
    if computer_score > 21:
        print("Computer went over. You win!")
        return

    print(f"Your cards: {user_card}")
    status = True

    while status:
        question = input("Type 'y' to get another card, type 'n' to pass: ")
        if question == "y":
            user_card.append(random.randint(0, 12))
            user_score = sum(user_card)
            print(f"Your cards: {user_card}")
            if user_score > 21:
                print("You went over. You lose!")
                return
        elif question == "n":
            status = False
        else:
            print("Please type 'y' or 'n'.")

    user_score = sum(user_card)
    computer_score = sum(computer_card)
    if computer_score < 17:
        computer_card.append(random.randint(0, 12))
        computer_score = sum(computer_card)

    print(f"Your final hand: {user_card}, final score: {user_score}")
    print(f"Computer's final hand: {computer_card}, final score: {computer_score}")

    if user_score > 21:
        print("You went over. You lose!")
    elif computer_score > 21:
        print("Computer went over. You win!")
    elif user_score > computer_score:
        print("You win!")
    elif user_score < computer_score:
        print("You lose!")
    else:
        print("It's a draw!")



start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
while start == "y":
    game()
    start = input("Do you want to play again? Type 'y' or 'n': ")

print("Thank you for playing Blackjack!")