from asyncio.windows_events import NULL
from tkinter import N
from unicodedata import name


class Player:
    def __init__(self):
        name = self
        playPile = []
        wonPile = []
    def playCard(self):
        if getSize(playPile) == 0:
            useWonPile()
        if getSize(playPile) > 0:
           return playPile.nextCard
        return NULL
    def getName():
        return name
    def collectCard(c):
        wonPile.addCards(p)
    def useWonPile():
        playPile.clear()
        playPile.addCards(wonPile)
        wonPile.clear()
    def numCards():
        return playPile.getSize() + wonPile.getSize()
    def __playPile__(self):
        return playPile
    def __wonPile__(self):
        return wonPile
    def __name__(self):
        return name
