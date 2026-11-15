import random
cards = {
    "Ace": 11,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "Jack": 10,
    "Queen": 10,
    "King": 10,
}
def deal_card():
    card = random.choice(list(cards.keys()))
    return card

def calculate_score(card_in_hand):
    card = []
    for i in card_in_hand:
        card.append(cards[i])
    if sum(card) == 21 and len(card) == 2:
        return 0
    elif 11 in cards and sum(card) > 21:
        card.remove(11)
        card.append(1)
    return sum(card)

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "You lose"
    elif user_score == 0:
        return "You win"
    elif user_score > 21:
        return "You lose"
    elif computer_score > 21:
        return "You win"
    elif user_score > computer_score:
        return "You win"
    else:
        return "You lose"

def game_start():
    user_cards = []
    computer_cards = []
    game_over = False
    computer_score = -1
    user_score = -1

    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while game_over is False:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your choice:{user_cards}")
        print(f"User Score:{user_score}")
        print(f"Computer 1st card:{computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
            print(f"You lose! Your final score was {user_score}")
        else:
            new_card = input("Do you want to play again? (Y/N)").lower()
            if new_card == "y" :
                user_cards.append(deal_card())
            else:
                game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your cards:{user_cards} and Your total score: {user_score}")
    print(f"Computers final hand: {computer_cards} and Computer total score: {computer_score}")
    print(compare(user_score, computer_score))

new_game = input("Do you want to play Blackjack? (Y/N)").lower()
if new_game == "y":
    game_start()
