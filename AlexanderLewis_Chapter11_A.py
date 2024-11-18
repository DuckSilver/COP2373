# import needed modules
import random

# initializes the cards
class Cards:
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        return f"{self.value} of {self.suit}"

# The core functions of poker
class Game:
    def __init__(self):
        self.cards = [Cards(value, suit) for suit in Cards.suits for value in Cards.values]
        self.shuffle()

    # deals cards
    def deal(self, num_cards=5):
        deal_cards = self.cards[:num_cards]
        self.cards = self.cards[num_cards:]
        return deal_cards

    # draws a card
    def draw(self, num_cards):
        drawn_cards = self.cards[:num_cards]
        self.cards = self.cards[num_cards:]
        return drawn_cards

    # randomizes cards
    def shuffle(self):
        random.shuffle(self.cards)

# Runs the game
def start_poker():
    cardDeck = Game()
    myDeck = cardDeck.deal(5)

    # prints inital deck
    print("Your Deck: ")
    for card in myDeck:
        print(f" {card}")

    cont = "0"

    while cont == "0":
        # replaces the inputed cards
        replace = input("Enter the card number(s) to be replaced (example: 1, 2, 5): ")
        list_replace = [int(x) - 1 for x in replace.split(",")]
        for index in list_replace:
            if 0 <= index < 5:
                print(f"Replacing {myDeck[index]}...")
                newCard = cardDeck.draw(1)[0]
                myDeck[index] = newCard
                cont = "1"
            else:
                print(f"Invalid card, please choose a number between 1 and 5")
                print(" ")

    # prints final deck
    print("Your final deck: ")
    print("Your Deck: ")
    for card in myDeck:
        print(f" {card}")

start_poker()









