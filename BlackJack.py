#Card deck of 52 cards
"""
types of cards
-----------
Clubs      C
Diamonds   D
Spades     S
Hearts     H

"""

import random as rn
#Ace Class

class Ace:
    def __init__(self,typ,value):
        self.typ = typ
        self.value = 1
        
    #function to print card
    def __str__(self):
        return ("Ace (%s) of %s"%(self.value,self.typ))
    
    #function to return class indicator
    def indi(self):
        return (True)
        
#Face Cards
class FaceCard:
    def __init__(self,typ,name,value):
        self.typ = typ
        self.value = value
        self.name = name
    #function to print card
    def __str__(self):
        return ("%s of %s"%(self.name,self.typ))
    
    #function to return class indicator
    def indi(self):
        return (False)

#Normal Cards (Cards from 2 to 10)
class Card:
    def __init__(self,typ,value):
        self.typ = typ
        self.value = value
        
    #function to print the card   
    def __str__(self):
        return ("%s of %s"%(self.value,self.typ))
    
    #function to return class indicator
    def indi(self):
        return (False)

#deck of cards

deck = []
typOfCard = ['Club','Diamonds','Spades','Hearts']
faceCards = ['King','Queen','Joker']
for x in typOfCard:
    ace = Ace(x,0)
    deck.append(ace)
    for i in range(2,11):
        crd = Card(x,i)
        deck.append(crd)
    for i in faceCards:
        crd = FaceCard(x,i,10)
        deck.append(crd)
#print(len(deck))

#player attributes

class Player:
    def __init__(self,name,bankBal):
        self.name = name
        self.bankBal = int(bankBal)
        
    def __str__(self):
        return ("%s has %d left in Bank balance"%(self.name,self.bankBal))

#function to display dealer's cards
def deal_game(lst):
    print("-=-=-=-=-=-=-=-")
    print("Time for dealer's Cards")
    for i in lst:
        print (i)

#total function for player

def psum(x):
    tot = 0
    for i in x:
        tot += i.value
    return tot

#hit or stand function

def res(lst):
    x = input("Give H for HIT and S for stand :- ")
    while True:
        if x.upper() not in ['H','S']:
            x = input("Please give a valid input :- ")        
        else:
            break
    if x.upper() == 'H' :
        lst.append(rn.choice(deck))
        deck.remove(lst[len(lst)-1])
    elif x == 's' or x == 'S':
        return x.upper()

#fnction to check wheather there is ace in card
#ac = ace checker
def ac(lst):
    for i in range(len(lst)):
        if lst[i].indi() == True :
            return i    

#ace value decider
#av = ace value
def av(lst):
    if ac(lst) != None and psum(lst) < 21:
        lst[ac(lst)].value = 11

#Playing Table

print("Welcome to Black Jack")
name = input("Your name please :- ")
print("Your starting bank balance is $1000")
val = 1000
p1 = Player(name,val)
print(p1)
 
#player's cards
"""pc = []

for i in range(2):
    pc.append(rn.choice(deck))
    deck.remove(pc[i])"""
#winner = 'unknown'

while True:
    winner = 'unknown'
    #print(len(deck))
    while True:
        bet = int(input("Make your bet please :- "))

        while True:
            if bet > p1.bankBal:
                print("Sorry Not Enought Balance \n Please make new bet ")
                bet = int(input(" :- "))
            elif type(bet) != int or bet == 0:
                print("Please make a valid bet")
                bet = int(input(" :- "))
            else:
                break
        print("Your bet is %d \n "%(bet))
        
        pc = []

        for i in range(2):
            pc.append(rn.choice(deck))
            deck.remove(pc[i])
            
        print('***********')
        for i in pc:
            print (i)
        print('***********')
        #print(ac(pc))
        av(pc)
        if (psum(pc) == 21):
            print("Black Jack!!!!")
            winner = p1.name
            break

        #dealer's Cards
        dc = []

        for i in range(2):
            dc.append(rn.choice(deck))
            deck.remove(dc[i])
        print("\n")
        print("Dealer has a :- %s " %(dc[0]))
        av(dc)
        if (psum(dc) == 21):
            print("Dealer is the Black Jack")
            winner = 'DEALER'
            break

        while True:
            print("\n")
            #print("\n")
            a = res(pc)
            if psum(pc) == 21:
                print("**************")
                print("Perfect 21!!")
                print("**************")
                for i in pc:
                    print(i)
                winner = p1.name
                break
            elif psum(pc) > 21:
                print("--X--X--X--X--X--X--")
                print("Oppsii!! You Brust")
                print(psum(pc))
                for i in pc:
                    print(i)
                deal_game(dc)
                winner = 'DEALER'
                break
            elif (a == 'S'):
                for i in pc:
                    print (i)
                deal_game(dc)
                if (psum(pc) > psum(dc)):
                    winner = p1.name
                elif (psum(pc) < psum(dc)):
                    winner = 'DEALER'
                elif psum(pc) == psum(dc):
                    print("So its a tie")
                    winner = 'NA'
                break 
            print("****NEW DECK****")
            for i in pc:
                print(i)
        if winner == 'DEALER':
            p1.bankBal -= bet
            print("*****LOSS*****")
        elif winner == p1.name:
            p1.bankBal += bet
            print("*****WIN*****")
        print("You have %d"%(p1.bankBal))
        break
    print("***END OF ROUND***")
    dec = input("one more?? (Y/N):- ")
    if dec.upper() =="N":
        break
    elif p1.bankBal <= 0:
        print("Ah!! Not enough balance")
        break