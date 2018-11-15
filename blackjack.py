#
# basic text based blackjack game.
#


import random


SUITS = ("hearts", "clubs", "diamonds", "spades")
RANKS = ("A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2", "1")
VALUES = {"A": 11, "K": 10, "Q": 10, "J": 10, "10": 10, "9": 9,
          "8": 8, "7": 7, "6": 6, "5": 5, "4": 4, "3": 3, "2": 2, "1": 1}


# main logic of the game
def main():
    continue_playing = True
    game_deck = Deck()
    game_deck.shuffle_deck()
    # print(game_deck)
    print_rules()

    player1 = Player("Player 1")
    dealer = Player("Dealer")
    players = [player1, dealer]

    while continue_playing:
        # create player1, deal the player and run the player's hand

        print(("\n" * 100) + "PLAYER 1, IT IS YOUR TURN!")
        player1.initial_deal(game_deck.cards)
        player1.show_hand()
        player1.print_total()
        while True:
            if player1.total_of_hand() == 21:
                print("\tBLACKJACK!")
                break
            elif player1.total_of_hand() > 21:
                print("\tBUST!")
                break
            selection = input("Press (H) to Hit, (S) to Stand")
            if "h" in selection.lower():
                player1.hit(game_deck.cards)
                player1.show_hand()
                player1.print_total()
            else:
                print("\tSTAY!")
                break

        input("\nPress enter to continue...")

        # only deal to dealer if player didn't bust
        if player1.total_of_hand() <= 21:
            print(("\n" * 100) + "DEALER, IT IS YOUR TURN!")
            # deal the dealer, and run dealer's hand
            dealer.initial_deal(game_deck.cards)
            while True:
                dealer.show_hand()
                dealer.print_total()
                if dealer.total_of_hand() == 21:
                    print("\tBLACKJACK!")
                    break
                elif dealer.total_of_hand() > 21:
                    print("\tBUST!")
                    break
                elif dealer.total_of_hand() < 17:
                    # dealer must hit anything under 17
                    dealer.hit(game_deck.cards)
                else:
                    # dealer will stay if not won, bust or under 17
                    print("\tSTAY!")
                    break
        else:
            print("\nDealer not dealt because player 1 busted.")

        input("\nPress enter to continue...")

        # determine winner
        show_winner(players)

        # determine of game should continue
        continue_playing = continue_playing_question()

    final_results(players)


# object class for player. each object has a hand. eventually can add bankroll and player details
class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.wins = 0
        self.losses = 0
        self.total = 0

    # initial deal of two cards, pops the cards selected from the deck. returns the hand and the remaining deck
    def initial_deal(self, game_deck):
        # reset total and hand at each initial deal
        self.total = 0
        self.hand = []
        i = 0
        while i != 2:
            # loop twice to pull two cards, grabbing the bottom card each time
            self.hand.append(game_deck[0])
            game_deck.pop(0)
            i += 1

        return game_deck

    def show_hand(self):
        string_of_hand = ""
        for card in self.hand:
            string_of_hand = string_of_hand + " " + str(card)
        print("\t" + self.name + "'s hand: " + string_of_hand)
        return

    def hit(self, game_deck):
        self.hand.append(game_deck[0])
        game_deck.pop(0)
        print("\tHIT")
        return game_deck

    # very time this is called, total will reset and be recalculated
    def total_of_hand(self):
        total = 0
        # total up hand. need logic to handle face cards.
        for card in self.hand:
            if card.rank == "A" and total + card.value > 21:
                total += 1
            else:
                total += card.value
        return total

    def print_total(self):
        print("\t" + self.name + "'s total: " + str(self.total_of_hand()))
        return


class Deck:
    def __init__(self):
        self.cards = []
        for suit in SUITS:
            # not using the suites logic yet. Only used for getting right number of cards in the deck
            for rank in RANKS:
                self.cards.append(Card(suit, rank))

    def __str__(self):
        string = ""
        for card in self.cards:
            string += (str(card) + ", ")
        return string

    # takes list as parameter, shuffles it, and returns the shuffled list
    def shuffle_deck(self):
        random.shuffle(self.cards)
        return


# eventually will rewrite for each card to be an object.
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        # set value based on global dictionary's value for this rank
        self.value = VALUES[self.rank]

    def __str__(self):
        return "[" + str(self.rank) + " of " + self.suit + "]"


# show final results of game
def final_results(players):
    print(("\n" * 100) + "FINAL GAME RESULTS:")
    for player in players:
        print("{}\n\tWINS\tLOSSES".format(player.name))
        print("\t{}\t\t{}".format(player.wins, player.losses))


# show the winner of the game
def show_winner(players):
    player = players[0]
    dealer = players[1]
    # show round results and print winner
    print(("\n" * 100) + "ROUND RESULTS:")
    for user in players:
        user.show_hand()
        user.print_total()

    if player.total_of_hand() == dealer.total_of_hand():
        print("TIE!")
    elif player.total_of_hand() > 21:
        # player busted
        print("DEALER WINS!")
        player.losses += 1
        dealer.wins += 1
    elif dealer.total_of_hand() > 21:
        # dealer busted
        print("PLAYER WINS!")
        player.wins += 1
        dealer.losses += 1
    elif dealer.total_of_hand() < player.total_of_hand():
        print("PLAYER WINS!")
        player.wins += 1
        dealer.losses += 1
    else:
        print("DEALER WINS!")
        player.losses += 1
        dealer.wins += 1


# print the rules of the game
def print_rules():
    print("*************************************")
    print("*             BLACKJACK             *")
    print("*************************************")
    print("* Rules:                            *")
    print("* 1. Ace is auto-set to 11 or 1     *")
    print("* 2. Dealer always HIT if under 17  *")
    print("* 3. Tie games are a push           *")
    print("*************************************")
    input("\n\tPress enter to continue...")


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
