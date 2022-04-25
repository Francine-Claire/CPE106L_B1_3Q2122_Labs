class Pile:
    def __init__(self, front, end):
        self.pile = []
        self.front = 0
        self.end = 0 
    def getSize(self):
        return self.end-self.front
    def clear(self): 
        self.front = 0
        self.end = 0
    def addCard(self, c):
        self.pile[self.end] = c
        self.end += 1 
    def addCards(self, p):
        while self.p > 0:
            self.addCard(p.nextCard())
    def nextCard(self):
        if self.front == self.end:
            return NULL
        self.c = self.pile[self.front]
        self.front += 1
        return self.c


