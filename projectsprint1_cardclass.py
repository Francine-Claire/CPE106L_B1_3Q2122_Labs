class Card ():
    suit = ['Hearts','Clubs','Spades','Diamonds']
    rank = ['Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace']
    value = {'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':11,'Queen':12,'King':13,'Ace':14}

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = value[rank]

    def __str__(self):
        return self.rank + 'of' + self.suit

    def __gt__(self,other):
        if self.rank == 1:
            self.rank = 14
        if other.rank == 1:
            other.rank = 14

        if self.rank > other.rank:
            return True
        return False

    def __lt__(self,other):
        if self.rank== 1:
            self.rank = 14
        if other.rank == 1:
            other.rank = 14

        if self.rank < other.rank:
            return True
        return False

    def __eq__(self,other):
        if self.rank == 1:
            self.rank = 14
        if other.rank == 1:
            other.rank = 14

        if self.rank == other.rank:
            return True
        return False





        
