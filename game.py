'''
Created on Feb 28, 2019


Name: Dhruv Gupta & Michael Xu
Snapshot #2: Game is working, but need to make it look nice (fix spacing).
Still need to play game more and try to look for more bugs. Also need to test out the Royal Flush. 

'''
from card import Card
from stack_of_cards import StackOfCards
from player import Player
from tkinter import *
from tkinter.tix import COLUMN


# These are the winning hands in order of strength
WINNING_HANDS = [ "Royal Flush", \
                  "Straight Flush", \
                  "Four of a Kind", \
                  "Full House", \
                  "Flush", \
                  "Straight", \
                  "3 of a Kind", \
                  "Two Pairs", \
                  "Pair (Jacks or better)"]

#===========================================================================
# Methods:
#     getValue - Returns value, A becomes a value of 14
#     __eq__ - Enables to check if two cards are equal
#     __lt__ - Allows comparison between two cards
#===========================================================================

class PokerCard(Card):
    def __init__(self,rank,suit):
        super().__init__(rank,suit)
        
    def getValue(self):
        if self.rank=="A":
            return 14
        else:
            return super().getValue()
        
    def __eq__(self,other):
        #NTBT
        if other.getValue()==self.getValue():
            return True
        else:
            return False
    
    def __lt__(self,other):
        #NTBT
        if self.getValue()<other.getValue():
            return True
        else:
            return False
        
#===========================================================================
# Methods:
#     sort - Returns sorted cards
#     getCards - Returns cards
#     suitCheck - Returns a boolean, checking whether
#     the suit of the currents cards is the same
#     handType - Checks what type of hand s currently in cards and returns string
#===========================================================================

class PokerHand(StackOfCards):
        
    def __init__(self):
        super().__init__()
        
    def sort(self):
        return self.cards.sort()
    
    def getCards(self):
        return self.cards
    
    def suitCheck(self):
        hand=self.getCards()
                
        for num in range(5):
            if hand[0].getSuit()!=hand[num].getSuit():
                return False
        return True
        
    
    def handType(self): 
        hand=self.getCards()
        hand.sort()
        

        #Royal Flush: 250
        rf=[10,11,12,13,14]
        check=True
        if self.suitCheck():
            for num in range(5):
                if hand[num].getValue()!=rf[num]:
                    check=False
                    break
                
            if check:
                return WINNING_HANDS[0]
                    
        #Straight Flush: 50
        check=True
        if self.suitCheck():
            for num in range(4): #Don't make it run 5 times because it'll compare the last one to nothing
                currentVal=hand[num].getValue()
                if hand[num].getValue()+1!=hand[num+1].getValue():
                    check=False
            
            if check:
                return WINNING_HANDS[1]
            
        check=True 
        #Four of a Kind: 25
        #77778
        #89999
        
        for num in range(4):
            og=hand[0].getValue()
            if og!=hand[num].getValue():
                for num in range(4,1,-1):
                    og=hand[-1].getValue()
                    if og!=hand[num-1].getValue():
                        check=False
        
        if check:
            return WINNING_HANDS[2]

        #Full House: 9
        #22233
        #22333
        if hand[0].getRank()==hand[1].getRank():
            if hand[0].getRank()==hand[2].getRank() and hand[3].getRank()==hand[4].getRank():
                return WINNING_HANDS[3]
            elif hand[2].getRank()==hand[3].getRank() and hand[2].getRank()==hand[4].getRank():
                return WINNING_HANDS[3]
            
        check=True
        #Flush: 6  
        if self.suitCheck():
            return WINNING_HANDS[4]
        
        #Straight: 4
        check=True
        for num in range(4): #Don't make it run 5 times because it'll compare the last one to nothing
            currentVal=hand[num].getValue()
            if hand[num].getValue()+1!=hand[num+1].getValue():
                check=False
                break
            
        if check:
            return WINNING_HANDS[5]
            
        #3 of a Kind: 3
        if hand[0].getRank()==hand[1].getRank() and hand[0].getRank()==hand[2].getRank():
            return WINNING_HANDS[6]
        if hand[1].getRank()==hand[2].getRank() and hand[1].getRank()==hand[3].getRank():
            return WINNING_HANDS[6]
        if hand[2].getRank()==hand[3].getRank() and hand[2].getRank()==hand[4].getRank():
            return WINNING_HANDS[6]
        
        #Two Pairs: 2
        #11255
        #11225
        #12233
        if hand[0].getRank()==hand[1].getRank():
            if hand[3].getRank()==hand[4].getRank() or hand[2].getRank()==hand[3].getRank():
                return WINNING_HANDS[7]
        if hand[1].getRank()==hand[2].getRank() and hand[3].getRank()==hand[4].getRank():
            return WINNING_HANDS[7]
        
        #Pair (Jacks or better): 1
        for num in range(4):
            if hand[num].getRank()==hand[num+1].getRank():
                if hand[num].getValue()>=11 and hand[num+1].getValue()>=11:
                    return WINNING_HANDS[8]
            
        return "Nothing"
                        
#===========================================================================
# Methods:
#     askHoldChoice - Prints what cards the player has held
#===========================================================================
class PokerPlayer(Player):
    
    def __init__(self,name,amt,cards):
        super().__init__(name,amt,cards)
        
    def askHoldChoice(self,player):
        #NTBT
        holdPos=input("Which card(s) would you like to hold (ex. 1 4 5)?")
        
        check=True
        while check:
            temp=holdPos.replace(" ","")
            if not(temp.isdigit()) and not(temp=="") and not(len(set(temp))==len(temp)):
                print("Sorry, but that's an invalid input!")
                holdPos=input("Which card(s) would you like to hold (ex. 1 4 5)?")
            else:
                for val in temp:
                    if int(temp)>5:
                        print("Sorry, but that's an invalid input!")
                        holdPos=input("Which card(s) would you like to hold (ex. 1 4 5)?")
                check=False
                    
        print("You held: ",end="")
        
        if temp=="":
            print("Nothing!",end="")
                        
        for i in range(len(temp)):
            if temp[i]=="1":
                print(player.getCard(0),end="")
                print(" ",end="")
            elif temp[i]=="2":
                print(player.getCard(1),end="")
                print(" ",end="")
            elif temp[i]=="3":
                print(player.getCard(2),end="")
                print(" ",end="")
            elif temp[i]=="4":
                print(player.getCard(3),end="")
                print(" ",end="")
            elif temp[i]=="5":
                print(player.getCard(4),end="")
                print(" ",end="")
                
        return holdPos
  
class GUI():
    def __init__(self,win):
        self.win=win
        self.win.title("Poker Game")
        self.win.configure(background="RoyalBlue3")
        
        
        self.label=Label(self.win,text="Poker Game")
        
        self.infoLabel=Label(self.win,text="Enter your name & credits. Ex: Dhruv, 100",bg="RoyalBlue3",fg="yellow",font="helvetica 14 bold")
        self.infoLabel.grid(row=1,column=0,sticky=W)
        
        self.infoEntry=Entry(self.win,width=20,bg="white")
        self.infoEntry.grid(row=2,column=0,sticky=W)
        
        self.infoBut=Button(self.win,text="Submit",width=6,command=self.clickInfo)
        self.infoBut.grid(row=3,column=0,sticky=W)
        self.hc=[1,1,1,1,1]
        self.suit=""
        self.count=0
        
        
    def pokerGame(self):
        self.player=PokerPlayer(self.name,int(self.credits),PokerHand())
        self.deck=PokerHand()
        
        #Display initial credits
        self.gameTitle=Label(self.win,text="Credits:",bg="RoyalBlue3",fg="yellow",font="impact 20 bold")
        self.gameTitle.grid(row=0,column=0,sticky=W)
        self.credLabel=Label(self.win,text=self.player.getMoney(),bg="RoyalBlue3",fg="yellow",font="impact 20 bold")
        self.credLabel.grid(row=0,column=1,sticky=W)
        
        for suit in ['♥', '♦', '♣', '♠']:
            for rank in ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']:
                self.deck.add(PokerCard(rank,suit))
        self.deck.shuffle()
        
        self.PlayRound()
        
    
        
    def PlayRound(self):
        self.player.addMoney(-1)
        #Image Variables
        self.images=[]
        self.rimages=[]
        self.count+=1
        
        #Deal cards to player
        for i in range(5):
            self.player.addCard(self.deck.deal())
                    
            if self.player.getCard(i).getSuit()=="♥":
                self.suit="H"
            elif self.player.getCard(i).getSuit()=="♦":
                self.suit="D"
            elif self.player.getCard(i).getSuit()=="♣":
                self.suit="C"
            else:
                self.suit="S"
                
            image=PhotoImage(file="PNG/"+str(self.player.getCard(i).getValue())+self.suit+".png")
            self.images.append(image)
        
        self.player.hand.sort()
        
        #Resizing the images
        self.rimages.append(self.images[0].subsample(3,3))
        self.rimages.append(self.images[1].subsample(3,3))
        self.rimages.append(self.images[2].subsample(3,3))
        self.rimages.append(self.images[3].subsample(3,3))
        self.rimages.append(self.images[4].subsample(3,3))
        
        #Card buttons
        self.card1=Label(self.win,image=self.rimages[0])
        self.card1.grid(row=1,column=1,sticky=W)
        
        self.card2=Label(self.win,image=self.rimages[1])
        self.card2.grid(row=1,column=2,sticky=W)
        
        self.card3=Label(self.win,image=self.rimages[2])
        self.card3.grid(row=1,column=3,sticky=W)
        
        self.card4=Label(self.win,image=self.rimages[3])
        self.card4.grid(row=1,column=4,sticky=W)
        
        self.card5=Label(self.win,image=self.rimages[4])
        self.card5.grid(row=1,column=5,sticky=W)
        
        #Hold buttons
        if self.count==1: #Prevents repeat buttons which cause error
            self.holdBut1=Button(text="Hold",width=6,command=self.holdInfo1)
            self.holdBut1.grid(column=1,row=2)
            
            self.holdBut2=Button(text="Hold",width=6,command=self.holdInfo2)
            self.holdBut2.grid(column=2,row=2)
            
            self.holdBut3=Button(text="Hold",width=6,command=self.holdInfo3)
            self.holdBut3.grid(column=3,row=2)
            
            self.holdBut4=Button(text="Hold",width=6,command=self.holdInfo4)
            self.holdBut4.grid(column=4,row=2)
            
            self.holdBut5=Button(text="Hold",width=6,command=self.holdInfo5)
            self.holdBut5.grid(column=5,row=2)
            
        self.drawBut=Button(text="Draw",command=self.drawInfo,font="impact 25")
        self.drawBut.grid(column=3,row=4)
        
    def drawInfo(self):
        sub=0
        
        if self.count>2:
            self.winLabel.destroy()
            
        #Remove Unwanted Cards
        for val in range(5):
            if self.hc[val]==0:
                self.player.hand.remove(val-sub)
                sub+=1
        
        #Add new cards  
        for i in range(sub):
            self.player.addCard(self.deck.deal())
        self.player.hand.sort()
        
        if sub!=0:
            #Empty images
            self.images=[]
            self.rimages=[]
            
            #Make new images
            for i in range(5):
                
                if self.player.getCard(i).getSuit()=="♥":
                    self.suit="H"
                elif self.player.getCard(i).getSuit()=="♦":
                    self.suit="D"
                elif self.player.getCard(i).getSuit()=="♣":
                    self.suit="C"
                else:
                    self.suit="S"
                  
                image=PhotoImage(file="PNG/"+str(self.player.getCard(i).getValue())+self.suit+".png")
                self.images.append(image)
            
            #Resizing images 
            self.rimages.append(self.images[0].subsample(3,3))
            self.rimages.append(self.images[1].subsample(3,3))
            self.rimages.append(self.images[2].subsample(3,3))
            self.rimages.append(self.images[3].subsample(3,3))
            self.rimages.append(self.images[4].subsample(3,3))
            
            #Card images
            self.card1=Label(self.win,image=self.rimages[0])
            self.card1.grid(row=1,column=1,sticky=W)
            
            self.card2=Label(self.win,image=self.rimages[1])
            self.card2.grid(row=1,column=2,sticky=W)
            
            self.card3=Label(self.win,image=self.rimages[2])
            self.card3.grid(row=1,column=3,sticky=W)
            
            self.card4=Label(self.win,image=self.rimages[3])
            self.card4.grid(row=1,column=4,sticky=W)
            
            self.card5=Label(self.win,image=self.rimages[4])
            self.card5.grid(row=1,column=5,sticky=W)
            
        #Winning hand
        self.winType=self.player.hand.handType()
        self.winLabel=Label(text=self.winType+"!!",bg="RoyalBlue3",fg="yellow",font="impact 20 bold")
        self.winLabel.grid(row=3,column=0)
        
        #Add money
        
        if self.winType==WINNING_HANDS[0]:
            self.player.addMoney(250)
        elif self.winType==WINNING_HANDS[1]:
            self.player.addMoney(50)
        elif self.winType==WINNING_HANDS[2]:
            self.player.addMoney(25)
        elif self.winType==WINNING_HANDS[3]:
            self.player.addMoney(9)
        elif self.winType==WINNING_HANDS[4]:
            self.player.addMoney(6)
        elif self.winType==WINNING_HANDS[5]:
            self.player.addMoney(4)
        elif self.winType==WINNING_HANDS[6]:
            self.player.addMoney(3)
        elif self.winType==WINNING_HANDS[7]:
            self.player.addMoney(2)
        elif self.winType==WINNING_HANDS[8]:
            self.player.addMoney(1)
            
        self.credLabel.destroy()        
        self.credLabel=Label(self.win,text=self.player.getMoney(),bg="RoyalBlue3",fg="yellow",font="impact 20 bold")
        self.credLabel.place(x=70,y=0)
        
        #New deck
        self.deck=PokerHand()
        for suit in ['♥', '♦', '♣', '♠']:
            for rank in ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']:
                self.deck.add(PokerCard(rank,suit))
        self.deck.shuffle()
        
        #Remove old cards
        for i in range(5):
            self.player.hand.remove(0)

        self.dealBut=Button(text="Deal",command=self.PlayRound,font="impact 25")
        self.dealBut.grid(column=3,row=4)
            
            
            
    def clickInfo(self):
        self.infoText=self.infoEntry.get()
        self.infoText.replace(" ","")
        pos=self.infoText.find(",")
        self.name=self.infoText[:pos]
        self.credits=self.infoText[pos+1:]
        self.infoEntry.destroy()
        self.infoBut.destroy()
        self.infoLabel.destroy()
        self.pokerGame()
        
    def holdInfo1(self):
        if self.holdBut1.config("text")[-1]=="Hold":
            self.holdBut1.config(text="Discard")
            self.hc[0]=0
        else:
            self.holdBut1.config(text="Hold")
            self.hc[0]=1
            
    def holdInfo2(self):
        if self.holdBut2.config("text")[-1]=="Hold":
            self.holdBut2.config(text="Discard")
            self.hc[1]=0
        else:
            self.holdBut2.config(text="Hold")
            self.hc[1]=1
    
    def holdInfo3(self):
        if self.holdBut3.config("text")[-1]=="Hold":
            self.holdBut3.config(text="Discard")
            self.hc[2]=0
        else:
            self.holdBut3.config(text="Hold")
            self.hc[2]=1
            
    def holdInfo4(self):
        if self.holdBut4.config("text")[-1]=="Hold":
            self.holdBut4.config(text="Discard")
            self.hc[3]=0
        else:
            self.holdBut4.config(text="Hold")
            self.hc[3]=1
            
    def holdInfo5(self):
        if self.holdBut5.config("text")[-1]=="Hold":
            self.holdBut5.config(text="Discard")
            self.hc[4]=0
        else:
            self.holdBut5.config(text="Hold")
            self.hc[4]=1
"""        
root=Tk()
gui=GUI(root)
root.mainloop()
"""

        
def PokerGame():

    print("Welcome to Video Poker!")
    name=input("What is your name?")
    print("Hello, "+name+", let's begin")
    credits=input("How many credits are you playing with?")
    
    #Input Validation
    check=True
    while check:
        if not(credits.isdigit()):
            print("Sorry, but that's an invalid input!")
            credits=input("How many credits are you playing with?")
        else:
            check=False
    
    print("You have "+credits+" credits\n")
    
    deck=PokerHand()
    player=PokerPlayer(name,int(credits),PokerHand())
    
    for suit in ['♥', '♦', '♣', '♠']:
        for rank in ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']:
            deck.add(PokerCard(rank,suit))
            
    deck.shuffle()
    
    playRound(player,deck)
    
    check=True
    while check:
        cont=input("Would you like to continue playing? (y/n)")
        if cont=="y":
            print()
            deck=PokerHand()
            for suit in ['♥', '♦', '♣', '♠']:
                for rank in ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']:
                    deck.add(PokerCard(rank,suit))
            deck.shuffle()
            playRound(player,deck)
        elif cont=="n":
            exit()
        else:
            print("That's an invalid input try again")
        
    
def playRound(player,deck):
    #Starting round price
    player.addMoney(-1)
    
    #Deal cards
    for i in range(5):
        player.addCard(deck.deal())
    player.hand.sort()
    print(player)
    
    #Hold cards & Print cards
    hold=player.askHoldChoice(player)
    cardsHeld=len(hold.replace(" ",""))
    
    #Deal new hand & Replace unwanted cards
    sub=0
    for i in range(5):
        if not(str(i+1) in hold):
            player.hand.remove(i-sub)
            sub+=1
            
    for i in range(5-cardsHeld):
        player.addCard(deck.deal())

    #Type of hand & Winning credits
    winType=player.hand.handType()
    
    check=True
    
    if winType==WINNING_HANDS[0]:
        player.addMoney(250)
        credWon=250
    elif winType==WINNING_HANDS[1]:
        player.addMoney(50)
        credWon=50
    elif winType==WINNING_HANDS[2]:
        player.addMoney(25)
        credWon=25
    elif winType==WINNING_HANDS[3]:
        player.addMoney(9)
        credWon=9
    elif winType==WINNING_HANDS[4]:
        player.addMoney(6)
        credWon=6
    elif winType==WINNING_HANDS[5]:
        player.addMoney(4)
        credWon=4
    elif winType==WINNING_HANDS[6]:
        player.addMoney(3)
        credWon=3
    elif winType==WINNING_HANDS[7]:
        player.addMoney(2)
        credWon=2
    elif winType==WINNING_HANDS[8]:
        player.addMoney(1)
        credWon=1
    elif winType=="Nothing":
        credWon=0
        check=False

    print()
    player.addMoney(credWon)
    print(player)
    if check:
        print(winType+" You won "+str(credWon)+"!! credits")
    else:
        print("Nothing... You lost!")
    print("You have "+str(player.getMoney())+" left")
    
    #Clear players hand
    for i in range(5):
        player.hand.remove(0)

    return winType
    
def main():
    c=input("Would you like to play the GUI version or Text version(1/2)")
    if c=="1":
        win=Tk()
        gui=GUI(win)
        win.mainloop()
    elif c=="2":
        PokerGame()
    
    
if __name__ == "__main__":
    main() 


