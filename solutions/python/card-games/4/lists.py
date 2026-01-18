"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number):
    rounds = []
    rounds.append(number)
    rounds.append(number + 1)
    rounds.append(number +2)
    return rounds


def concatenate_rounds(rounds_1, rounds_2):
    return rounds_1 + rounds_2


def list_contains_round(rounds, number):
    return number in rounds


def card_average(hand):
    return sum(hand) / len(hand)


def approx_average_is_average(hand):
    hand_average = sum(hand) / len(hand)
    nums_average = (hand[0] + hand[-1]) / 2
    median_element = len(hand) // 2
    return hand_average == nums_average or hand_average == sorted(hand)[median_element]
    

def average_even_is_average_odd(hand):
    even_index_values = hand[::2]  
    odd_index_values = hand[1::2] 
    average_even = sum(even_index_values) / len(even_index_values)
    average_odd = sum(odd_index_values) / len(odd_index_values)
    return average_even == average_odd

def maybe_double_last(hand):
    if hand[-1] == 11:
        hand[-1] = hand[-1] * 2
        return hand
    return hand
    