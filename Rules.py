#put this after is surrounding
def removestones(board,x,y,player_color,oppisttisecolor,board_size=19):
    visitboard = [[False for _ in range(board_size)] for _ in range(board_size)]
    return dfs_clear(board,x,y,visitboard,player_color,oppisttisecolor,True,0)



def dfs_clear(board, x, y, visitboard, player_color, oppisttisecolor, isinfactsurrounded,points):

        if not is_out_of_bounds(board, x, y) and not board[x][y] == oppisttisecolor and visitboard[x][y] == False:
            board[x][y] = ' '
            visitboard[x][y] = True
           # prisoners += 1
            isinfactsurrounded = dfs_clear(board, x + 1, y, visitboard, player_color, oppisttisecolor, isinfactsurrounded,points)
            isinfactsurrounded = dfs_clear(board, x, y + 1, visitboard, player_color, oppisttisecolor, isinfactsurrounded,points)
            isinfactsurrounded = dfs_clear(board, x, y - 1, visitboard, player_color, oppisttisecolor, isinfactsurrounded,points)
            dfs_clear(board, x - 1, y, visitboard, player_color, oppisttisecolor, isinfactsurrounded, points)

        return board

def rule_enforcement(board,x,y,playercolor,oppisttisecolor):

    global copyboard
    board[x][y] = playercolor
    if iscapturing(board, x, y, playercolor, oppisttisecolor):
     copyboard = copy_board(board)
     removestones(board, x, y, playercolor, oppisttisecolor) #but also save a copy just in case
     if ko_check(board, copyboard):
         # invalid move
         return copyboard,False
    if not issurrounded(board, x, y, playercolor, oppisttisecolor):
     return board,True
    return board,True


def blackplace(board,x,y):
    waslegal=False
    if board[x][y] == ' ':
     board,waslegal=rule_enforcement(board,x,y,'X','O')
    return board,waslegal


def whiteplace(board,x,y):
    waslegal = False
    if board[x][y] == ' ':
     board,waslegal=rule_enforcement(board,x,y,'O','X')
    return board,waslegal

def issurrounded(board,x,y,player_color,oppisttisecolor,board_size=19):
    visitboard = [[False for _ in range(board_size)] for _ in range(board_size)]
    return dfs(board,x,y,visitboard,player_color,oppisttisecolor,True)



def dfs(board,x,y,visitboard,player_color,oppisttisecolor,isinfactsurrounded):
 if not isinfactsurrounded:
     return False

 if board[x][y] == ' ':
     return False #liberty found, stop searching


 if not is_out_of_bounds(board,x,y) and not board[x][y] == oppisttisecolor and visitboard[x][y] == False:
    visitboard[x][y] = True
    isinfactsurrounded = dfs(board,x+1,y,visitboard,player_color,oppisttisecolor,isinfactsurrounded)
    isinfactsurrounded =  dfs(board,x,y+1,visitboard,player_color,oppisttisecolor,isinfactsurrounded)
    isinfactsurrounded =  dfs(board,x,y-1,visitboard,player_color,oppisttisecolor,isinfactsurrounded)
    isinfactsurrounded =  dfs(board,x-1,y,visitboard,player_color,oppisttisecolor,isinfactsurrounded)



 return isinfactsurrounded


def is_out_of_bounds(board,x,y):
    return x>=len(board) or y>=len(board) or x<0 or y<0


def ko_check(board,prevoiusboard):

 for i in board:
     for j in board[i]:
      if board[i][j] != prevoiusboard[i][j]:
       return False #is not a duplicate of the prevoius board

 #note: check this for only single captures, ko doesn't apply when two or more are captured
 return True

def copy_board(board):
    return board

def iscapturing(board,x,y,player_color,oppisttisecolor,board_size=19):
  #will absolutely need to test this later, but i think this might work.
    visitboard = [[False for _ in range(board_size)] for _ in range(board_size)]
    # we want to reverse the situation we want to check if opponent is surrounded
    if not is_out_of_bounds(board,x+1,y) and board[x+1][y]==oppisttisecolor:
     return dfs(board, x+1, y, visitboard, oppisttisecolor,player_color, True)
    if not is_out_of_bounds(board,x-1,y) and board[x-1][y]==oppisttisecolor:
        return dfs(board, x - 1, y, visitboard, oppisttisecolor, player_color,True)
    if not is_out_of_bounds(board, x , y+1) and board[x][y+1] == oppisttisecolor:
        return dfs(board, x, y+1, visitboard,  oppisttisecolor,player_color, True)
    if not is_out_of_bounds(board, x, y - 1) and board[x][y - 1] == oppisttisecolor:
        return dfs(board, x, y - 1, visitboard, oppisttisecolor, player_color, True)
    return False