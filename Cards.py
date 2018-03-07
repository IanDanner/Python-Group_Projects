import random
class Deck(object):

    def __init__(self):
        self.cards= []
        self.suits= ['heart','diamond','spade','club']
        self.ranks= ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
        for rank in self.ranks:
            for suit in self.suits:
                self.cards.append(Card(rank, suit))
    
    def shuffle(self,num):
        for count in range(0,num):
            for idx in range(0,len(self.cards)):
                temp = self.cards[idx]
                temp2 = random.randint(0,51)
                self.cards[idx] = self.cards[temp2]
                self.cards[temp2] = temp
        return self

    def deal(self,val):
        hand = []
        amt = 0
        while amt < val:
            rand = len(self.cards)-1
            if hand.count(self.cards[rand]) == 0:
                hand.append(self.cards[rand])
                self.cards.pop()
                hand[amt].printMe()
                amt += 1
        return self

class Card(object):

    def __init__(self,jsuit,jrank):
        self.suit = jsuit
        self.rank = jrank

    def printMe(self):
        print self.suit,self.rank
        return self
    
deck1 = Deck()

deck1.shuffle(5).deal(7)