Skip to content
Search or jump to…

Pull requests
Issues
Marketplace
Explore
 
@MattRBilek 
Learn Git and GitHub without any code!
Using the Hello World guide, you’ll start a branch, write comments, and open a pull request.


MattRBilek
/
ProjectCodeSpring2021GameAI
forked from tmgall/ProjectCodeSpring2021GameAI
0
01
Code
Pull requests
Actions
Projects
Wiki
Security
Insights
Settings
ProjectCodeSpring2021GameAI/ConnectFour/minmax.py /
@MattRBilek
MattRBilek Create minmax.py
…
Latest commit 69b41f9 2 days ago
 History
 1 contributor
43 lines (39 sloc)  1.7 KB
  
#REQ get games returns the possible moves from game state
#REQ cost gets cost of game [-1, 1] 1 means player to move losing to get [0,1] to [-1,1] just do (score * 2) - 1, 0 assumes tieing
import Game
def miniMax(game, depth):
  return miniMaxhelp(getGames(game),depth)[1] # returns the best board state from current given board

def miniMaxhelp(gameArr, depth):
  for board in gameArr:
    if board.getWinner(): # get winner returns true when there is one winner
      return (1,board,0)
  if depth == 0: # reached lowest level get best score
    maxCost = cost(gameArr[0])
    maxboard = gameArr[0]
    for i in range(1,len(gameArr)): # calculate best board from current possition
      temp = cost(gameArr[i])
      if temp > minCost:
        maxCost = temp
        maxboard = gameArr[i]
    return (maxCost,maxboard,0) # return best score

  r = (0, gameArr[0],1) # first game
  temp = getGames(gameArr[0])
  if (len(temp)!=0): 
    r = miniMaxhelp(temp, depth -1) # calls minimax for first game in gameArr
    r = (r[0] * -1, gameArr[0], r[2] + 1)

  for i in range(1,len(gameArr)): # check for the rest of the game
    temp = getGames(gameArr[i])
    hold = r;
    if len(temp) != 0: # if there are sub games get the best
      hold = miniMaxhelp(temp, depth - 1)
      hold = (hold[0] * -1, gameArr[i], hold[2] + 1)
    else:
      hold = (0, gameArr[i], 0) # no possible games assume we tied as we have not won yet

    if (hold[0] > r[0]): # if new score is better take new score
      r = hold
    elif (hold[0] == r[0]):
      if hold[0] > 0 and hold[2] < r[2]: # if we are in a winning line take shortest path
        r = hold
      elif hold[2] > r[2]: # if we are in a losing line take longest path
        r = hold
  return r
© 2021 GitHub, Inc.
Terms
Privacy
Security
Status
Docs
Contact GitHub
Pricing
API
Training
Blog
About
