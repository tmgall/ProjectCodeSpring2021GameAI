import numpy as np
from Game import Game


t = Game()
while not t.getOver():
    t.place(int(input()))
    if not t.getOver():
        t.place(t.getBestMove())
    t.printBoard()
    print('\n')

