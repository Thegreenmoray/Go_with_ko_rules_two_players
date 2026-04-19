from flask import Flask, render_template,request, jsonify

import Go
import Rules

# Create an instance of the Flask class
app = Flask(__name__)
board = Go.createboard(19)
# Define a route for the home page
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/board",methods=['GET'])
def counterrtitory():
 global board
 black, white, netural = Rules.countterritory(board)
 return jsonify({ 'black': black, 'white': white, 'netural': netural })





@app.route('/move', methods=['POST'])
def makemove():
    global board
    data = request.get_json()
    row = data.get('row')
    col = data.get('col')
    player = data.get('player')
    new_board,waslegal= Rules.whiteplace(board,row,col) if player=='O' else Rules.blackplace(board,row,col)
    board = new_board
    return jsonify({ 'waslegal': waslegal ,
        'next_player': 'O' if player == 'X' else 'X' ,
                     'board': board })



# Run the app locally
if __name__ == "__main__":
   app.run()