##playingcards.py
#Anil Timbil, Francisco Guerrero
#COM 110 Assignment 5
#Due date:Sun Nov 6 2016
#This module creates the playing cards neccessary for playing Blackjack.
#This module will be used in the other modules to be able to create the
#Blackjack game. 

from graphics import *

class playingcards:
    def __init__(self,rank,suit):   #initiates the class rank and suit
        """This function holds the characteristics reached at the playing cards.
        Rank is the number value of the playing cards,
        Suit is either diamond, club, heart and spade"""
        self.rank = rank
        self.suit = suit

    def getRank(self):  #returns the rank of the card
        return self.rank

    def getSuit(self):    #returns the suit of the card
        return self.suit

    def BJValue(self):   #returns the Blackjack value of a card
        if self.rank > 10:  #if the card is bigger than 10 (Jack Quenn King)
                            # their value is changed to 10.
            value = 10 
            return value
        else: 
            return self.rank
        

    def __str__(self):    #returns a string for the card
        Listrank = [1,2,3,4,5,6,7,8,9,10,11,12,13]
        suits ={"d":"Diamonds","h":"Hearts","c":"Clubs","s":"Spades"}
        listsuits=list(suits.items())
       
        for rank in Listrank:   #It goes through every rank and suit
            if self.rank == rank:
                for i in range(len(listsuits)):
                    if (listsuits[i])[0] == self.suit: #matches the appropriate suits 
                        if rank==1:
                            return ("Ace of "+(listsuits[i])[1])
                        elif rank==11:
                            return ("Jack of "+(listsuits[i])[1])
                        elif rank==12:
                            return ("Quenn of "+(listsuits[i])[1])
                        elif rank==13:
                            return ("King of "+(listsuits[i])[1])
                        else:
                            return (str(rank)+" of "+(listsuits[i])[1])
        

def main():                           
    x=playingcards(12,"s")
    print(x.BJValue())
    print(x.BJValue())
    print(x.__str__())

if __name__ == '__main__':
    main()
                            
            
