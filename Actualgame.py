from tkinter import Tk, Label, Button
import tkinter as tk
import Go
import Rules
from Player import Player

root = Tk()
player1 = Player('X')#black
player2 = Player('O')#white
label1 = Label(root, text='insert colors turn')  # obviously replace this with the color whos turn it is
board=Go.createboard(19)#allow user to change board size eventually
isplaying=False
canvas_size = 300
margin = 10
board_size = len(board)
cell_size = (canvas_size - 2 * margin) / (board_size - 1)



def endgame():
    global isplaying
    global board
    board=None
    isplaying=False
    #count the prisioners (and maybe terrority)



button = Button(root, text='pass',command=endgame)
button.pack()

def startgui():
    root.title('Go with Ko rules')
    root.geometry('500x500')
    label1.place(x=10,y=10)
    button = Button(root, text='start',command=startgame)
    button.pack()
    root.mainloop()




#def editboard(board):
  #  for i in board:
   #     for j in board[i]:
     #label blackstone    if board[i][j] == 'X' else label whitestone if board == 'O' else done


def startgame():
    matrix_frame = tk.Frame(root)
    matrix_frame.pack(padx=10, pady=10)
    canvas = tk.Canvas(root, width=300, height=300, bg="#F0D095")
    margin =10
    sizeboard=len(board)
    cell_size = (300 - 2 * margin) / ( sizeboard- 1)
    canvas.pack()
    for i in board:
        canvas.create_line(margin + i * cell_size, margin,
                                 margin + i * cell_size, 10 + (sizeboard - 1) * cell_size)
        canvas.create_line(margin, margin + i * cell_size,
                           margin + (sizeboard - 1) * cell_size, margin + i * cell_size)

    # print out board

def whitemove(event):
    global board
    global isplaying
    if (isplaying):
        x = event.x
        y = event.y
        # find a way to make it so the x and y cooridantes can be matched to the intersections Maybe divide by board row/column?

        boardget = board
        boardnewboard, islegal = Rules.whiteplace(boardget, x, y)  # probably should add this with players to count prisoners but this is fine for now
        board = boardnewboard
        # update display
        if islegal:
            blackturn()

def blackmove(event):
 global board
 global isplaying
 if(isplaying):
     x=event.x
     y=event.y
     #find a way to make it so the x and y cooridantes can be matched to the intersections Maybe divide by board row/column?
     #fixing_X=300-2*

     boardget=board
     boardnewboard,islegal= Rules.blackplace(boardget,x,y) #probalby should add this with players to count prisoners but this is fine for now
     board=boardnewboard
     #update display
     if islegal:
         whiteturn()


def blackturn():
    global label1
    root.unbind('<Mouse1>')
    root.bind('<Mouse1>', blackmove)
    label1.config(text="Black's turn")
    # update label with black turn

def whiteturn():
    global label1
    root.unbind('<Mouse1>')
    root.bind('<Mouse1>', whitemove)
    label1.config(text="White's turn")
    #update label with whites turn

def ingame():
    global isplaying
    isplaying = True
    root.bind('<Mouse1>',blackmove)


startgui()


