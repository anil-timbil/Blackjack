#Deck.py
#Anil Timbil, Francisco Guerrero
#COM 110 Assignment 5
#Due date:Sun Nov 6 2016
#This module will create a deck that will be used to deal cards. Then, it will
#keep track of the cards in the deck. Using this module enables us to create a deck,
#shuffle it, deal a card from the deck, count the number of cards left in the deck
#and return the rank and suit of the cards.

from graphics import *
from playingcards import *
from random import *

"""Attributes of this Deck class are as follows.
   INSTANCE VARIABLES

   self.cardList: A list of appended playing cards
   self.permList: An unaltered list of playing cards
   self.card:  First cards delt from the deck
   """

class deck:
    def __init__(self): #initiates class deck()
        self.cardList = []# Initiate the list
        numberofranks=13
        Listsuit=["c","d","h","s"]
        
        for suit in Listsuit:
            for rank in range(1,numberofranks+1):
                card=playingcards(rank,suit)
                cardstr=card.__str__()
                self.cardList.append(cardstr)
        self.permList=self.cardList  #to have a permanent list of cards. This list is unshuffled.
                                    #so that we can get the rank and suit of the card
                                    #when we deal a random card.
    def constructor(self):
        return self.cardList #returns constructed card list

    def shuffle(self):   #this function will be used to shuffle the constructed card list
        shufflecards = []#this list will store all card indexes to identify unshuffled cards
        ShuffleDeck =[]  #this list will hold the final deck of shuffled cards
        for i in range(52):
            x=randrange(0,52)
            while x in shufflecards: #while loop will check for the presence of a card within the index list
                x=randrange(0,52)
            shufflecards.append(x)
            randomcard=self.cardList[x] #finds a random card within the card list
            ShuffleDeck.append(randomcard)
        self.cardList=ShuffleDeck
        return self.cardList

    def dealCard(self): #this functioni will be used to deal and track a new card
        self.card=self.cardList[0]
        self.cardList.pop(0) #delete delt card from deck
        #print(self.cardList)  test print
        
        return self.card

    def cardsLeft(self): #returns lenght of deck after a card has been delt
        return len(self.cardList)

    def getSuit(self): #returns the suit of a card from a list of ordered cards
        if self.card in self.permList[:13]: #first cards are clubs
            suit="c"
        if self.card in self.permList[13:26]: #next 13 are diamonds
            suit="d"
        if self.card in self.permList[26:39]: #following 13 are hearts
            suit="h"
        if self.card in self.permList[39:52]: #last 13 are spades
            suit="s"

        return suit

    def getRank(self): #returns the ranks of a card
        if (self.permList.index(self.card)<13): #returns index of card +1 (since index starts from 0
            self.rank = (self.permList.index(self.card)+1)
        #for following elif statesments, any extra sets of suits beyond 13 are subtracted to track true value
        elif (self.permList.index(self.card)<26):
            self.rank = (self.permList.index(self.card)-13+1)

        elif (self.permList.index(self.card)<39):
            self.rank = (self.permList.index(self.card)-26+1)

        elif (self.permList.index(self.card)<52):
            self.rank = (self.permList.index(self.card) -39 +1)

        return self.rank
    
    def getBJValue(self): #determines blackjack value of each card
        if self.rank > 10:
            self.rank = 10 ### added
            return self.rank ###
        else: ###
            return self.rank 
        
                       
def main():
    x=deck()
    print(x.constructor())
    #print(len(x.constructor()))
    print(x.shuffle())

    
    print(x.dealCard())
    print(x.getSuit())
    print(x.getRank())
    print(x.getBJValue())

    print(x.cardsLeft())
    
if __name__ == '__main__':
    main()
 
            
            
