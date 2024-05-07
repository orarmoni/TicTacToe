# Tic Tac Toe Game with Flask-SocketIO

This project implements a real-time Tic Tac Toe game using Python with Flask-SocketIO for the backend. Players can make moves on a 3x3 game board, and the game state is synchronized in real-time between multiple clients.

## Dependencies
- Flask
- Flask-SocketIO

## Setup
1. Install the requirements from  requirements.txt


## Installation
1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/your_username/tic-tac-toe.git



Run the server:
python app.py


Run client:
open client.html on your favorite browser

Implementation:

Game Logic:
The game logic is implemented in Python on the server side.
Each move made by a player updates the game board state stored on the server.
After each move, the server checks for a winner by examining the current state of the game board. If a winning condition is met, the server emits a win event to all clients, indicating the winner.
If all cells are filled and no winner is found, the game is declared a draw, and the server emits a game_over event to all clients.

Winning Combinations Definition:
The function defines the winning combinations as a list of lists, where each inner list represents a winning combination.
For example, [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]] represents all possible winning combinations in Tic Tac Toe.

Real-time Communication:
Flask-SocketIO handles real-time communication between the server and clients using WebSocket connections.
When a player makes a move, the server broadcasts the updated game state to all connected clients, ensuring that the game board is synchronized in real-time across multiple browsers.
Events such as update_board, win, and game_over are emitted by the server and listened to by clients to update the game interface accordingly.

