from flask import Flask, request, jsonify
from flask_socketio import SocketIO, emit
import json
from time import sleep
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
socketio = SocketIO(app)
socketio.init_app(app, cors_allowed_origins="*")


board = ['' for _ in range(9)]
current_player = 'X'
num_of_moves = 0


def check_winner():
    # Define winning combinations
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6] # Diagonals
    ]
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != '':
            return board[combo[0]]
    return 0

@socketio.on('makeMove')
def makeMove(msg):
    global current_player, board, num_of_moves
    index = msg.get('position',-1)
    if board[index] == '':
        print(index)
        board[index] = current_player
        if current_player == 'X':
            current_player = 'O'
        else:
            current_player = 'X'
        emit('update_board', {'board': board, 'turn': current_player}, broadcast=True)
        sleep(0.1)
        res = check_winner()
        if res:
            emit('win', {'winner': res}, broadcast=True)
            reset()
            return
        num_of_moves = num_of_moves + 1
        print(num_of_moves)
        if num_of_moves == 9:
           emit('game_over', broadcast=True) 
    else:
        return jsonify({'message': 'Invalid move! Please choose an empty cell.'}), 400


@socketio.on('restart')
def reset():
    global board, current_player, num_of_moves
    board = ['' for _ in range(9)]
    current_player = 'X'
    num_of_moves = 0
    emit('update_board', {'board': board, 'turn': current_player}, broadcast=True)



if __name__ == '__main__':
    app.run(debug=True)
