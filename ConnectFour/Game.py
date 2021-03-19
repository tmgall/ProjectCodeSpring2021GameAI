import numpy as np 

class Game:
    self.board = np.zeros(42)
    self.over = False
    self.winner = 0

    def getBoard(self):
        return self.board 
    
    def getOver(self):
        return self.over 
    
    def getWinner(self):
        return self.winner 
    
    def printBoard(self):
        # the board is 7 columns wide and 6 rows tall 
        # index the board starting from the bottom left
        # so, the bottom left is 0, the bottom right is 6, the top right is 41, etc
        pass 

    def canPlace(self):
        pass

    def place(self, spot, turn):
        pass

    def checkForWin(self):
        pass

    def checkForDraw(self):
        pass

    def updateState(self):
        # check for a win and update if there is one
        # check for a draw and update if there is one
        pass

    def getBestMove(self):
        pass

    def minimax(self, depth, maximizing):
        # if a certain depth is exceeded, call evaluateState to get filler value
        pass

    def evaluateState(self):
        # if no winner, hard code a way of evaluating board state in a basic way
        pass 

