import copy



def removestones(board, captured_positions):
        for row, col in captured_positions:
            board[row][col] = ' '
        return board
#
#test next
def rule_enforcement(board,x,y,playercolor,oppisttisecolor):

    global copyboard
    working_board = copy.deepcopy(board)
    working_board[x][y] = playercolor
    copyboard = copy_board(board) #used to compare later
    capturing,captured_coordinates=iscapturing(working_board, x, y, playercolor, oppisttisecolor)
    if capturing:
     working_board =removestones(working_board,captured_coordinates)
    if not hasliberties(working_board, x, y, playercolor, oppisttisecolor) and not capturing:
     return board, False

    if ko_check(working_board, copyboard):
         # invalid move
         return board,False

    return working_board,True

def blackplace(board,x,y):
    waslegal=False
    board_copy = copy.deepcopy(board)
    if not is_out_of_bounds(board_copy, x, y)and board_copy[x][y] == ' ':
     resulting_board,waslegal=rule_enforcement(board_copy,x,y,'X','O')
     return resulting_board, waslegal
    return board_copy,waslegal

def whiteplace(board,x,y):
    waslegal = False
    board_copy = copy.deepcopy(board)
    if not is_out_of_bounds(board_copy, x, y)and board_copy[x][y] == ' ':
     resulting_board,waslegal=rule_enforcement(board_copy,x,y,'O','X')
     return resulting_board,waslegal
    return board_copy,waslegal
#tested
def hasliberties(board,x,y,player_color,oppisttisecolor,board_size=19):
    visitboard = [[False for _ in range(board_size)] for _ in range(board_size)]
    return dfs(board,x,y,visitboard,player_color,oppisttisecolor,True,[])

def dfs(board,x,y,visitboard,player_color,oppisttisecolor,isinfactsurrounded,captured_positions):
 if not isinfactsurrounded:
     return False,[]

 if is_out_of_bounds(board,x,y):
     return isinfactsurrounded,captured_positions


 if board[x][y] == ' ':
     return False,[] #liberty found, stop searching


 if not board[x][y] == oppisttisecolor and visitboard[x][y] == False:
    visitboard[x][y] = True
    captured_positions.append((x,y))
    isinfactsurrounded,captured_positions = dfs(board,x+1,y,visitboard,player_color,oppisttisecolor,isinfactsurrounded,captured_positions)
    isinfactsurrounded,captured_positions =  dfs(board,x,y+1,visitboard,player_color,oppisttisecolor,isinfactsurrounded,captured_positions)
    isinfactsurrounded,captured_positions =  dfs(board,x,y-1,visitboard,player_color,oppisttisecolor,isinfactsurrounded,captured_positions)
    isinfactsurrounded,captured_positions =  dfs(board,x-1,y,visitboard,player_color,oppisttisecolor,isinfactsurrounded,captured_positions)



 return isinfactsurrounded,captured_positions


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

def iscapturing(board, x, y, player_color, oppisttisecolor, board_size=19):
    visitboard = [[False for _ in range(board_size)] for _ in range(board_size)]
    all_captured = []

    # Check all four directions
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if not is_out_of_bounds(board, nx, ny) and board[nx][ny] == oppisttisecolor:
            is_surrounded, captured = dfs(board, nx, ny, visitboard, oppisttisecolor, player_color, True, [])
            if is_surrounded:
                all_captured.extend(captured)

    return len(all_captured) > 0, all_captured