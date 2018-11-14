#
# basic text based blackjack game.  UNDER CONSTRUCTION
#


import random


# list of cards in a standard deck of 52 cards.
DECK = ["A", "K", "Q", "J", 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, "A", "K", "Q", "J", 10, 9, 8, 7, 6, 5, 4, 3, 2, 1,
        "A", "K", "Q", "J", 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, "A", "K", "Q", "J", 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

# number of decks to be used for this game. want to give ability to use multiple decks in future versions of the game
NO_OF_DECKS = 1


# main logic of the game
def main():
    continue_playing = True
    game_deck = shuffle_deck(DECK)

    while continue_playing:
        # deal cards to player
        game_deck, player_hand = initial_deal(game_deck)
        print(game_deck)
        show_hand(player_hand)

        # option to hit, stay
        # possible outcome of round: bust, blackjack or stay

        # deal cards for dealer
        # dealer must hit anything under 17

        # determine winner

        # determine of game should continue
        continue_playing = continue_playing_question()


# hit, return new hand and modified deck
def hit(game_deck, hand):
    hand.append(game_deck[0])
    game_deck.pop(0)
    return game_deck, hand


def show_hand(the_hand):
    string_of_hand = ""
    for card in the_hand:
        string_of_hand = string_of_hand + " " + str(card)
    print("current hand: " + string_of_hand)
    return


def total_of_hand(the_hand):
    # total up hand. need logic to handle face cards.
    return


# initial deal of two cards, pops the cards selected from the deck. returns the hand and the remaining deck
def initial_deal(game_deck):
    hand = ["", ""]
    i = 0
    while i != 2:
        hand[i] = game_deck[0]
        game_deck.pop(0)
        i += 1

    return game_deck, hand


# takes list as parameter, shuffles it, and returns the shuffled list
def shuffle_deck(deck):
    random.shuffle(deck)
    return deck


# get user input and return boolean answer
def continue_playing_question():
    while True:
        choice = str(input("Would you like keep playing? (y or n)"))
        if "y" in choice.lower():
            return True
        elif "n" in choice.lower():
            return False


# if this file is being executed rather than imported, run main function
if __name__ == "__main__":
    main()

exit()
