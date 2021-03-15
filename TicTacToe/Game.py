import numpy as np

class Game:
    def __init__(self):
        self.board = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.winner = 0
        self.turn = True
        self.over = False

    def getOver(self):
        return self.over

    def getWinner(self):
        return self.winner

    def getTurn(self):
        return self.turn

    def printBoard(self):
        for i in range(3):
            for j in range(3):
                print(self.board[3 * i + j], end=' ')
            print("\n")

    def canPlace(self, spot):
        return self.board[spot] == 0

    def place(self, spot):
        if not self.canPlace(spot):
            return
        if self.turn:
            self.board[spot] = 1
        else:
            self.board[spot] = -1
        self.turn = not self.turn
        self.checkIfWin()
        if self.checkDraw():
            self.over = True
        if self.winner != 0:
            self.over = True

    def checkIfWin(self):
        for i in range(3):
            if self.board[3 * i] == 1 and self.board[3 * i + 1] == 1 and self.board[3 * i + 2] == 1:
                self.winner = 1
            if self.board[3 * i] == -1 and self.board[3 * i + 1] == -1 and self.board[3 * i + 2] == -1:
                self.winner = 2
            if self.board[i] == 1 and self.board[i + 3] == 1 and self.board[i + 6] == 1:
                self.winner = 1
            if self.board[i] == -1 and self.board[i + 3] == -1 and self.board[i + 6] == -1:
                self.winner = 2
        if self.board[0] == 1 and self.board[4] == 1 and self.board[8] == 1:
            self.winner = 1
        if self.board[0] == -1 and self.board[4] == -1 and self.board[8] == -1:
            self.winner = 2
        if self.board[2] == 1 and self.board[4] == 1 and self.board[6] == 1:
            self.winner = 1
        if self.board[2] == -1 and self.board[4] == -1 and self.board[6] == -1:
            self.winner = 2

    def checkDraw(self):
        for i in range(9):
            if self.board[i] == 0:
                return False
        if self.winner == 0:
            return True
        else:
            return False

    def toString(self):
        turnString = ""
        if self.turn:
            turnString = "1"
        else:
            turnString = "2"
        res = "The game is "
        if self.over:
            if self.winner == 0:
                "drawn."
            else:
                res += "over. The winner was Player " + str(self.winner)
        else:
            res += "not over."
        return res

    def copyGame(game):
        g = Game()
        g.board = np.array([i for i in game.board])
        g.turn = game.turn
        g.over = game.over
        g.winner = game.winner
        return g

    def getGames(self):
        arr = []
        for i in range(9):
            if self.canPlace(i):
                temp = self.copyGame()
                temp.place(i)
                arr.append(temp)
        return arr

    def getBestMove(self):
        def miniMaxhelp(gameArr):
            for board in gameArr:
                if board.getWinner():
                    return (1, board, 0)
            r = (0, gameArr[0], 0)
            temp = gameArr[0].getGames()
            if (len(temp) != 0):
                r = miniMaxhelp(temp)
                r = (r[0] * -1, gameArr[0], r[2] + 1)

            for i in range(1, len(gameArr)):
                temp = gameArr[i].getGames()
                hold = r
                if len(temp) != 0:
                    hold = miniMaxhelp(temp)
                    hold = (hold[0] * -1, gameArr[i], hold[2] + 1)
                else:
                    hold = (0, gameArr[i], 0)
                if (hold[0] > r[0]):
                    r = hold
                elif (hold[0] == r[0]):
                    if hold[0] == 1 and hold[2] < r[2]:
                        r = hold
                    elif hold[2] > r[2]:
                        r = hold
            return r
        b = miniMaxhelp(self.getGames())[1]
        num = 0
        for i in range(1, 9):
            if b.board[i] != self.board[i]:
                num = i
        return num
