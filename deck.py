# creating card class
class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        # parsing value of card to blackjack value
        try:
            self.compare_value = int(self.value)
        except ValueError:
            if self.value.lower == 'ace':
                pass
            self.compare_value = 10


# creating deck
DECK = list()
for suit in ['hearts', 'diamonds', 'clubs', 'spades']:
    DECK.append(Card('ace', suit))
    for value in range(2, 11):
        DECK.append(Card(str(value), suit))
    DECK.append(Card('jack', suit))
    DECK.append(Card('queen', suit))
    DECK.append(Card('king', suit))
