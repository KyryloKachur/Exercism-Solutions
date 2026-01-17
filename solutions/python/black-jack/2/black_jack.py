cards = {"J": 10, "Q": 10, "K": 10, "A": 1}

def value_of_card(card):
    if card == "A":
        return 1
    elif card in cards:
        return 10
    return int(card)
    
def higher_card(card_one, card_two):
    value_one = cards[card_one] if card_one in cards else int(card_one)
    value_two = cards[card_two] if card_two in cards else int(card_two)
    if value_one > value_two:
        return card_one
    elif value_two > value_one:
        return card_two
    return card_one, card_two
    
def value_of_ace(card_one, card_two):
    if card_one == "A" or card_two == "A":
        return 1 
    first_card = cards[card_one] if card_one in cards else int(card_one)
    second_card = cards[card_two] if card_two in cards else int(card_two)
    return 11 if first_card + second_card + 11 <= 21 else 1


def is_blackjack(card_one, card_two):
    has_ace = card_one == "A" or card_two == "A"
    has_ten = card_one in ["10", "J", "Q", "K"] or card_two in ["10", "J", "Q", "K"]
    return has_ace and has_ten


def can_split_pairs(card_one, card_two):
    first_card = cards[card_one] if card_one in cards else int(card_one)
    second_card = cards[card_two] if card_two in cards else int(card_two)
    if first_card == second_card:
        return True
    return False

def can_double_down(card_one, card_two):
    first_card = cards[card_one] if card_one in cards else int(card_one)
    second_card = cards[card_two] if card_two in cards else int(card_two)
    if first_card + second_card in range(9,12):
        return True
    return False

    
