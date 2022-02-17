import random
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

def calculate_score(cards):
    """take a list of cards and return the sum of all the cards in hand"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.append(1)
        cards.remove(11)
    return sum(cards)

def deal_cards():
    """return random card form deck """
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card

def compare(user_score , computer_score):
    if user_score ==  computer_score:
        return "Draw "
    elif computer_score == 0:
        return "Lose, opponent has Blackjack"
    elif user_score == 0:
        return "You Won"
    elif user_score > 21:
        return "You went over 21, you lose"
    elif computer_score > 21:
        return "You Won, computer has over 21"

    elif user_score > computer_score:
        return "You Won"
    else:
        return "You lose"


user_card = []
computer_card = []

is_game_over = False

for _ in range(2):
    user_card.append(deal_cards())
    computer_card.append(deal_cards())


while not is_game_over:

    user_score = calculate_score(user_card)
    computer_score = calculate_score(computer_card)

    print(f"Your cards: {user_card}, current total: {user_score}")
    print(f"Computer's cards: [{computer_card[0]},*]")

    if user_score == 0 or computer_score == 0 or user_score > 21:
        is_game_over = True
    else:
        user_another_card = input('Type "y" to get another card, type "n" to pass:' )
        if user_another_card == 'y':
            user_card.append(deal_cards())
        else:
            is_game_over = True


while computer_score != 0  and computer_score < 17:
    computer_card.append(deal_cards())
    computer_score = calculate_score(computer_card)

print(f"Your final hand: {user_card}, final score: {user_score}")
print(f"Computer's cards: {computer_card}, final score: {computer_score}")
compare(user_score,computer_score)
