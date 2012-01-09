from random import randint

#---------CLASS DEFINITION----------------------------------------------------------------------------


class Deck(object):
    
    def __init__(self):
        #define each suit in a list
        self.suit = [
            "Hearts",
            "Diamonds",
            "Clubs",
            "Spades"
        ]

        #define all cards as strings
        self.stringvalue = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace"]

        #define all card values
        self.realvalue = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]

        #define empty deck dictonary. Deck dictionary allow us to show String but use values during gameplay.
        self.deck_dict = {}

        #define an empty list to be the deck
        self.deck = []

    #Create the values for the dictionary. Creates each card, connects each written value of the card to the real value of the card
    def Create_Deck_Dict(self):
        current_string_value = 0
        for value in self.stringvalue:
            for suit in self.suit:
                current_card = value + ' of ' + suit
                self.deck_dict[current_card] = self.realvalue[current_string_value]
            current_string_value += 1
        return self.deck_dict

    #Create values for the deck list. Creates each card of every suit.
    def Create_Deck(self):
        for value in self.stringvalue:
            for suit in self.suit:
                self.deck.append(value + ' of ' + suit)
        return self.deck



class Create_Hand(object):

    def __init__(self, deck, deck_dict):
        self.deck = deck
        self.cards = [] #empty list of cards in this hand
        self.deck_dict = deck_dict
        
    def Create_Hand(self):
        create_card = [0, 1] #define list of cards to be created
        for num in create_card: #loop to create 2 cards
            self.cards.append(deck.pop(randint(0, len(deck)-1))) #add a random card from deck (first in range to last index in "deck") to "cards" list
            num += 1 
        return self.cards

    def Total(self, cards): #takes cards and returns the hard values. May change to return cards, not the total. 
        card1 = deck_dict[self.cards[0]] 
        card2 = deck_dict[self.cards[1]]
        return card1 + card2



class Game(object):
    def __init__(self, deck, deck_dict):
        self.deck = deck
        self.deck_dict = deck_dict

        self.player_cards = Create_Hand(deck, deck_dict) #Create_Hand object called in Game class. 
        self.cards = self.player_cards.Create_Hand() #cards = players cards
        self.total = self.player_cards.Total(self.cards) #total = cards total

    def DealUser(self):
        print "You are dealt \n" + self.cards[0] + '\n' + self.cards[1]
        print self.total

    #def DealDealer():
     #   print "The Dealer is dealt " +


#-----------------RUNTIME--------------------------------------------------------------------




#instantiate Deck obj
create_deck = Deck()
deck = create_deck.Create_Deck()
deck_dict = create_deck.Create_Deck_Dict()

game = Game(deck, deck_dict)
game.DealUser()



#-------------------DEBUG STUFF------------------------------------------------------------------

#create_hand = Create_Hand(deck, deck_dict)
#cards = create_hand.Create_Hand()
#print cards
#total = create_hand.Total()
#print total


#deal = Deal(cards, deck_dict)
#total = deal.Total()
#print total
