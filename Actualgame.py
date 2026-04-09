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
cell_size = round((canvas_size - 2 * margin) / (board_size - 1))
matrix_frame = tk.Frame(root)
matrix_frame.pack(padx=10, pady=10)
canvas = tk.Canvas(root, width=300, height=300, bg="#F0D095")

canvas.pack()
for i in range(board_size):
    canvas.create_line(margin + i * cell_size, margin,
                       margin + i * cell_size, 10 + (board_size - 1) * cell_size)
    canvas.create_line(margin, margin + i * cell_size,
                       margin + (board_size - 1) * cell_size, margin + i * cell_size)


def endgame():
    global isplaying
    global board
    root.unbind('<Button-1>')
    board=None
    isplaying=False
    #count the prisioners (and maybe terrority) nvm, do this when moving to flask



button = Button(root, text='pass',command=endgame)
button.pack()

def startgui():
    root.title('Go with Ko rules')
    root.geometry('500x500')
    label1.place(x=10,y=10)
    button = Button(root, text='start',command=startgame)
    button.pack()
    root.mainloop()


def editboard(board):
    canvas.delete("stone")
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 'X':
                draw_stone_other( i,j, "black", canvas, margin, cell_size)
            elif board[i][j] == 'O':
                draw_stone_other( i,j, "white", canvas, margin, cell_size)



def draw_stone_other(row, col, color, canvas, margin, cell_size):
    x = margin + row * cell_size
    y = margin + col * cell_size
    radius = cell_size * 0.4
    fill_color = "black" if color == "black" else "white"
    canvas.create_oval(x - radius, y - radius, x + radius, y + radius,
                       fill=fill_color, outline="black", tags="stone")


def startgame():

    ingame()
    # print out board

def whitemove(event):
    global board
    global isplaying
    global margin
    global board_size
    global cell_size
    if (isplaying and event.widget == canvas):
        x = event.x
        y = event.y
        x_adjusted=abs(round((x-margin)/cell_size))
        y_adjusted=abs(round((y-margin)/cell_size))
        print(x_adjusted,y_adjusted)


        if 0 <= x_adjusted < board_size and 0 <= y_adjusted < board_size and isplaying:
         boardget = board
         boardnewboard, islegal = Rules.whiteplace(boardget,x_adjusted,y_adjusted)  # probably should add this with players to count prisoners but this is fine for now
         board = boardnewboard

         if islegal and isplaying:
          editboard(board)
          blackturn()

def blackmove(event):
 global board
 global isplaying
 if(isplaying and  event.widget == canvas):
     x=event.x
     y=event.y
     #find a way to make it so the x and y cooridantes can be matched to the intersections Maybe divide by board row/column?
     x_adjusted = round((x-margin) / cell_size)
     y_adjusted = round((y-margin) / cell_size)
     print(x_adjusted, y_adjusted)#debug only
     # find a way to make it so the x and y cooridantes can be matched to the intersections Maybe divide by board row/column?

     if 0 <= x_adjusted < board_size and 0 <= y_adjusted < board_size and isplaying:
      boardget=board
      boardnewboard,islegal= Rules.blackplace(boardget,x_adjusted,y_adjusted) #probalby should add this with players to count prisoners but this is fine for now
      board = boardnewboard

      if islegal and isplaying:
         editboard(board)
         whiteturn()


def blackturn():
    global label1
    root.unbind('<Button-1>')
    root.bind('<Button-1>', blackmove)
    label1.config(text="Black's turn")
    # update label with black turn

def whiteturn():
    global label1
    root.unbind('<Button-1>')
    root.bind('<Button-1>', whitemove)
    label1.config(text="White's turn")
    #update label with whites turn

def ingame():
    global isplaying
    isplaying = True
    root.bind('<Button-1>',blackmove)


startgui()


