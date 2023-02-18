Hearts = ["Ace of Hearts", "2 of Hearts", "3 of Hearts", "4 of Hearts", "5 of Hearts", "6 of Hearts", "7 of Hearts", "8 of Hearts", "9 of Hearts", "10 of Hearts", "Jack of Hearts", "Queen of Hearts", "King of Hearts"]

Clubs = []
Clubs.append("Ace of Clubs")
Clubs.append("2 of Clubs")
Clubs.append("3 of Clubs")
Clubs.append("4 of Clubs")
Clubs.append("5 of Clubs")
Clubs.append("6 of Clubs")
Clubs.append("7 of Clubs")
Clubs.append("8 of Clubs")
Clubs.append("9 of Clubs")
Clubs.append("10 of Clubs")
Clubs.append("Jack of Clubs")
Clubs.append("Queen of Clubs")
Clubs.append("King of Clubs")

Spades = []
for i in range(2, 11):
    Spades.append(str(i)+" of Spades")

Spades.insert(0, "Ace of Spades")
Spades.append("Jack of Spades")
Spades.append("Queen of Spades")
Spades.append("King of Spades")

Diamonds = []
Diamonds.append("Ace of Diamonds")
for i in range(2, 11):
    Diamonds.append(str(i)+" of Diamonds")

Diamonds.append("Jack of Diamonds")
Diamonds.append("Queen of Diamonds")
Diamonds.append("King of Diamonds")

# for i in range(13):
#     print(Hearts[i])
# for i in range(10):
#     print(Hearts[i])
# for i in range(10, 13):
#     print(Hearts[i])

Deck = []
Suits = [Clubs, Diamonds, Hearts, Spades]
def build_deck():
    for i in range(4):
        for j in range(13):
            Deck.append(Suits[i][j])


build_deck()
# print(Deck[0:13])

def get_suit(card):
    x=card.split()[-1]
    return x

# print(get_suit(Deck[13]))

def get_value(card):
    x=card.split()[0]
    return x

# print(get_value(Deck[13]))

def same_value(card1, card2):
    x=get_value(card1)
    y=get_value(card2)
    if x == y:
         print(True)
         return True
    else:
        print(False)
        return False

# same_value(get_value(Deck[13]), get_value(Deck[27]))

def same_value_multiple(*cards):
    x=len(cards)
    if x == 0:
        print("No cards to compare value")
        return
    for i in range(1, x):
        if get_value(cards[0]) != get_value(cards[i]):
            print("Not all cards are the same value")
            return False
    print("All cards are the same value")
    return True

same_value_multiple(get_value(Deck[0]), get_value(Deck[13]), get_value(Deck[26]))


