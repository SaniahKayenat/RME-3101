import math
class tictactoe:
    def __init__(self,player,ai):
        self.board = [[None,None,None],
                     [None,None,None],
                     [None,None,None]]
        self.player = player
        self.ai = ai
    def is_board_full(self):
        cnt = 0
        for row in self.board:
            temp = row.count(None)
            cnt+=temp
        if cnt == 0:
            return 1
        else:
            return 0

    def evaluate(self):
        for i in range(len(self.board)): #row-column winner
            if self.board[i][0] == self.board[i][1] == self.board[i][2] and (self.board[i][0] != None and self.board[i][1] !=None and self.board[i][2] !=None):
                if self.board[i][0] == self.player:
                    return -1
                else:
                    return 1
        for i in range(len(self.board)):
            if self.board[0][i] == self.board[1][i] == self.board[2][i] and (self.board[0][i] !=None and self.board[1][i] !=None and self.board[2][i] !=None):
                if self.board[0][i] == self.player:
                    return -1
                else:
                    return 1
        if (self.board[0][0] == self.board[1][1] == self.board[2][2]) and (self.board[0][0]!= None and self.board[1][1] != None and self.board[2][2] != None) : #diagonal winner
            if self.board[0][0] == self.player:
                return -1
            else:
                return 1
        if (self.board[0][2] == self.board[1][1] == self.board[2][0]) and (self.board[0][2]!= None and self.board[1][1] != None and self.board[2][0] != None) : #diagonal winner
            if self.board[0][2] == self.player:
                return -1
            else:
                return 1
        
        if  self.is_board_full() == 1: #its a tie
            return 0
        
    def minimax(self,max_agent): #for the ai
        if self.evaluate() is not None:
            return self.evaluate()
        if max_agent == 1:
            v = -math.inf
            for row in range(3):
                for col in range(3):
                    if self.board[row][col] == None:
                        self.board[row][col] = self.ai
                        v= max(v,self.minimax(0))
                        self.board[row][col] = None
                        #print("MAX")
            #print(v)
            return v
        elif max_agent == 0:
            v = math.inf
            for row in range(3):
                for col in range(3):
                    if self.board[row][col] == None:
                        self.board[row][col] = self.player
                        v = min(v,self.minimax(1))
                        self.board[row][col] = None
                        #print("MIN")
            #print(v)
            return v
            
    
        
    def bestmove(self): #for my ai
        best_val = -math.inf
        best_move=(None,None) 
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == None:
                    self.board[row][col] = self.ai
                    current_val = self.minimax(0)
                    #print(current_val, (row, col))
                    self.board[row][col] = None
                    if current_val > best_val:
                        #print("here")
                        best_val = current_val
                        best_move = (row,col)
        #print(best_move)
        #print(best_val)
        return best_move



    def player_move(self):
        while True:
            print('Enter the row you wanna make your move in(1-3)\n')
            row = int(input())
            print('Enter the column you wanna make your move in(1-3)\n')
            col = int(input())
            row = row-1
            col = col - 1
            if self.board[row][col] == None:
                self.board[row][col] = self.player
                return
            else:
                print("This position is already filled. Please enter empty positions\n")


    def ai_move(self):
        move =  self.bestmove()
        #print(move)
        if move.count(None) == 0:
            self.board[move[0]][move[1]] = self.ai
            return
        return

print("Would you like to be player 'X' or player 'O'?\n")
player = input()
if player.upper() == 'X':

    game = tictactoe('X','O')
else:
    game = tictactoe('O','X')

while True:
    print('Your Turn: ')
    game.player_move()
    for row in game.board:
        print(row)
    if game.evaluate() == 1:
        print('You win!\n')
        break
    elif game.evaluate() == -1:
        print('AI wins!\n')
        break
    elif game.evaluate() == 0:
        print("Its a tie!\n")
        break

    print("Opponent's Turn: ")
    game.ai_move()
    for row in game.board:
        print(row)
    if game.evaluate() == -1:
        print('You win!\n')
        break
    elif game.evaluate() == 1:
        print('AI wins!\n')
        break
    elif game.evaluate() == 0:
        print("Its a tie!\n")
        break