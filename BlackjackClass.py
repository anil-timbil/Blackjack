#Blackjack.py
#Deck.py
#Anil Timbil, Francisco Guerrero
#COM 110 Assignment 5
#Due date:Sun Nov 6 2016
#This module will be used to run an actual game of blackjack
#We defined a new blackjack class and used previous modules to draw and run the actual
#game in the main function below. The attributes of this blackjack class are defined below
from graphics import *
from playingcards import *
from Deck import *
from buttonClass import *


"""Attributes of this Blackjack class are as follows.

       INSTANCE VARIABLES
 
        dealerHand: a list of PlayingCard objects representing the dealer's hand
        playerHand: a list of PlayingCard objects representing the player's hand
        playingDeck: a Deck object representing the deck of cards the game is being played with
       
       METHODS
      
        __init__(self, dHand=[], pHand=[])
            constructor that initializes instance variables
            it also gives the playingDeck an initial shuffle
        initDeal(self,gwin,xposD,yposD,xposP,yposP):
            deals out initial cards, 2 per player and
            displays dealer and player hands on graphical win
            xposD and yposD give initial position for dealer cards
            xposP and yposP are analogous
        hit(self, gwin, xPos, yPos)
            adds a new card to the player's hand and places it at xPos, yPos
        evaluateHand(self, hand)
            totals the cards in the hand (list) that is passed in and returns total
            (ace counts as 11 if doing so allows total to stay under 21)
        dealearPlays(self, gwin, xPos, yPos)
        
            dealer deals cards to herself, stopping when hitting "soft 17"
        getClosedCard(self)        
            It is used to get the value of the closed card
        drawClosedCard(self,xposD,yposD,gwin)
            After user hits the stand button, this function draws the closed card
        getPHand(self)
            This function returns a list that includes the values of cards in players hand
        getDHand(self)
            This function returns a list that includes the values of cards in dealers hand
    """

class Blackjack:
    def __init__(self, dHand=[], pHand=[]): #initiates blackjack class
        self.dHand=dHand
        self.pHand=pHand
        self.deckcreate=deck()
        self.deckcreate.shuffle()

    def initDeal(self,gwin,xposD,yposD,xposP,yposP): #deals out first four cards to dealer and player
        self.gwin=gwin

        #We define four cards using the dealCard function
        #we obtain each cards rank to import the image of each card from the playing
        #cards folder. We also used the blackjack value of each card to add to the
        #total value of the dealer and players hand
        card1=self.deckcreate.dealCard()
        self.rank1=self.deckcreate.getRank()
        self.BJValue1=self.deckcreate.getBJValue()
        self.card1RankSuit="playingcards/"+self.deckcreate.getSuit()+str(self.rank1)+".gif"
        
        card2=self.deckcreate.dealCard()
        self.rank2=self.deckcreate.getRank()
        self.BJValue2=self.deckcreate.getBJValue()
        card2RankSuit="playingcards/"+self.deckcreate.getSuit()+str(self.rank2)+".gif"

        card3=self.deckcreate.dealCard()
        self.rank3=self.deckcreate.getRank()
        self.BJValue3=self.deckcreate.getBJValue()
        card3RankSuit="playingcards/"+self.deckcreate.getSuit()+str(self.rank3)+".gif"
        
        card4=self.deckcreate.dealCard()
        self.rank4=self.deckcreate.getRank()
        self.BJValue4=self.deckcreate.getBJValue()
        card4RankSuit="playingcards/"+self.deckcreate.getSuit()+str(self.rank4)+".gif"

        #we draw cards 2-4
        #card 1 is the dealers 1st card and is not revealed until the player stands
        card2Image=Image(Point(xposD+100,yposD),card2RankSuit)
        card2Image.draw(self.gwin)

        card3Image=Image(Point(xposP,yposP),card3RankSuit)
        card3Image.draw(self.gwin)

        card4Image=Image(Point(xposP+100,yposP),card4RankSuit)
        card4Image.draw(self.gwin)

        self.dealerhand=[self.BJValue2] #self.BJValue1  exluding this value to close the card
        self.playerhand=[self.BJValue3,self.BJValue4]

    def getClosedCard(self): #returns value of hidden/closed card
        return self.BJValue1

    def drawClosedCard(self,xposD,yposD,gwin): #draws closed card after player stands
        card1Image=Image(Point(xposD,yposD),self.card1RankSuit)
        card1Image.draw(self.gwin)
        
    def hit(self, gwin, xPos, yPos): #draws a new card for player and adds its value to players score
        total=self.evaluateHand(self.playerhand)
         ## this is a random number, 
        if total<= 21:
            dealcard= self.deckcreate.dealCard() #deals randoms card
            dealcardRankSuit="playingcards/"+self.deckcreate.getSuit()+str(self.deckcreate.getRank())+".gif" #draws card drawn from deck
            dealcardBJValue=self.deckcreate.getBJValue()
            dealcardImage= Image(Point(xPos,yPos),dealcardRankSuit)
            dealcardImage.draw(gwin)
            total=total+dealcardBJValue
            #updates total value of players hand
            self.playerhand.append(dealcardBJValue)
        ######## if total >21 change all aces to 1....

    def getPHand(self): #returns list of value representing cards in players hand
        return self.playerhand

    def getDHand(self): #returns list of value representing cards in dealer's hand
        return self.dealerhand
        
    def evaluateHand(self, hand,closedcard=0): #returns value of players/dealers hand
        self.hand=hand # hand is going to be a list in this case
        self.total=closedcard
        self.AceTotal=0
        Subtract=True
        for cardVal in self.hand: #assigns value to card and adds to the total
            if (cardVal == 1) and self.total+11<=21: #this if statement addresses the issue of the value of Ace (1 or 11)
                cardVal=11
                self.AceTotal=self.AceTotal+1 #counts how many ace is calculated as 11
                self.total=self.total+cardVal
            
            elif self.total+cardVal>21 and Subtract: 
                self.total=self.total+cardVal-(self.AceTotal*10)#This line subtracts extra 10s from the total
                Subtract=False

            else:
                self.total=self.total+cardVal

        return self.total
    
    def dealerPlays(self, gwin, xPos, yPos): #simulates a dealers hand once the player stands
        total=self.evaluateHand(self.dealerhand)+self.getClosedCard()
        IncreaseX=False
        for i in range(10): ## this is a random number, 
            if total< 17: #dealer stops once it reaches soft 17
                dealercard=self.deckcreate.dealCard()
                dealercardRank=self.deckcreate.getRank()
                self.BJValue=self.deckcreate.getBJValue()
                dealercardRankSuit="playingcards/"+self.deckcreate.getSuit()+str(dealercardRank)+".gif"
                dealercardImage= Image(Point(xPos,yPos),dealercardRankSuit)
                dealercardImage.draw(gwin)
                total=total+self.BJValue
                IncreaseX=True
                self.dealerhand.append(self.BJValue)

            if IncreaseX:
                xPos=xPos+100 #adds 100 to the x coordinate for the following card drawn in the window

def main():
    a=Blackjack()
    win=GraphWin("Blackjack Game", 900,600) #draws window
    win.setBackground("darkgreen")
    Intro=Text(Point(400,150),"Welcome to the Blackjack Game. Click Deal to start the game!\n"+
               "Stand if you do not want to increase your total. Hit\n to get another card."+
               "Ace counts as 11 if doing so\n does not exceed 21.").draw(win)
    Intro.setStyle("bold")
    Intro.setSize(20)
    #identifies dealer side
    dealerSide=Text(Point(300,70),"Dealer").draw(win)
    dealerSide.setStyle("bold")
    dealerSide.setSize(20)
    #identifies player side
    playerSide=Text(Point(300,480),"Player").draw(win)
    playerSide.setStyle("bold")
    playerSide.setSize(20)
    #draws buttons necessary for game function
    HitButton=Button(win,50,70,Point(300,280),"Hit")
    StandButton=Button(win,50,70,Point(200,280),"Stand")
    DealButton=Button(win,50,70,Point(450,240),"Deal")
    PlayButton=Button(win,50,70,Point(450,305),"Play Again")
    QuitButton=Button(win,50,70,Point(750,50),"Quit")
    #buttons will activate once first cards are delt
    StandButton.deactivate()
    HitButton.deactivate()
    PlayButton.deactivate()
    
    closedcard=Image(Point(600,300),"playingcards/b2fv.gif")
    closedcard.draw(win)
    
    Again=True
    pt=win.getMouse() #initiates while loop
    xPos=400 #used when hit function to initiate x coordinate of first cards delt
             #to avoid reusing x coordinate for cards to be drawn
    while Again and not QuitButton.isClicked(pt): #exit button
        if DealButton.isClicked(pt): ##to deal for the first time
            Intro.undraw()
            a.initDeal(win,200,150,200,400)

            closedcard=Image(Point(200,150),"playingcards/b2fv.gif")
            closedcard.draw(win)
            
            DealButton.deactivate()
            StandButton.activate() #stand and hit button activated once cards are delt
            HitButton.activate()
            #evaluates and draws the total value of hands
            evalPHand=a.evaluateHand(a.getPHand())
            scoreP=Text(Point(400,480), "Total: "+str(evalPHand)).draw(win)
            scoreP.setStyle("bold")
            scoreP.setSize(14)

            evalDHand=a.evaluateHand(a.getDHand())
            scoreD=Text(Point(400,70), "Total: "+str(evalDHand)).draw(win)
            scoreD.setStyle("bold")
            scoreD.setSize(14)           
            
        elif StandButton.isClicked(pt): ## if stand button is clicked
            a.drawClosedCard(200,150,win) #reveals closed card
            a.dealerPlays(win,400,150)
            StandButton.deactivate()

            evalDHand=a.evaluateHand(a.getDHand(),a.getClosedCard()) #evaluates hand and adds closed cards value
            scoreD.setText("Total: "+str(evalDHand))

            HitButton.deactivate() #deactivates hitButton once player stands

            if evalDHand>21: #declares winner if dealer busts
                Result=Text(Point(400,550), "The dealer busts! Player wins!").draw(win)
                Result.setStyle("bold")
                Result.setSize(24)
                Result.setTextColor("red")
            else:#if dealer doesn't exceed 21, dealer and players hand are compared to determine winner
                if evalDHand>evalPHand:
                    Result=Text(Point(400,550), "The dealer wins!").draw(win)
                    Result.setStyle("bold")
                    Result.setSize(24)
                    Result.setTextColor("red")
                elif evalDHand<evalPHand:
                    Result=Text(Point(400,550), "Player wins!").draw(win)
                    Result.setStyle("bold")
                    Result.setSize(24)
                    Result.setTextColor("red")
                else:
                    Result=Text(Point(400,550), "The game is tied!").draw(win)
                    Result.setStyle("bold")
                    Result.setSize(24)
                    Result.setTextColor("red")

            PlayButton.activate()


        elif HitButton.isClicked(pt): #draws a new card for player
            a.hit(win, xPos, 400)
            xPos=xPos+100 #updates x coordinate for next card drawn

            evalPHand=a.evaluateHand(a.getPHand())
            scoreP.setText("Total: "+str(evalPHand))

            if evalPHand>21: #declares player as loser if player busts
                Result=Text(Point(400,550), "You bust! Dealer wins!").draw(win)
                Result.setStyle("bold")
                Result.setSize(24)
                Result.setTextColor("red")
                HitButton.deactivate()
                StandButton.deactivate()
                PlayButton.activate()

        elif PlayButton.isClicked(pt):
            win.close()
            main()
            Again=False
            
            
        if Again:
            pt=win.getMouse()

    if Again:
        win.close()


if __name__ == '__main__':
    main()

    
    
