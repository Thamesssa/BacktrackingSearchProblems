# Define the game state
class GameState:
    def __init__(self):
        self.board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.player = 1
    
    def check_game_over(self):
        # Check if there is a winning combination on the board
        winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
        for combination in winning_combinations:
            if self.board[combination[0]] == self.board[combination[1]] == self.board[combination[2]] != 0:
                return self.board[combination[0]]
        # Check if the board is full
        if 0 not in self.board:
            return -1
        return 0
    
    def get_possible_moves(self):
        # Return the list of empty squares on the board
        return [i for i, square in enumerate(self.board) if square == 0]
    
    def make_move(self, move):
        # Make a move on the board and switch the player
        self.board[move] = self.player
        self.player = 3 - self.player
    
    def undo_move(self, move):
        # Undo a move on the board and switch the player back
        self.board[move] = 0
        self.player = 3 - self.player
    
    def get_result(self, player):
        # Return 1 if the player wins, -1 if the player loses, and 0 if it's a draw
        result = self.check_game_over()
        if result == player:
            return 1
        elif result == -1:
            return 0
        else:
            return -1

# Define the Mini Max function
def mini_max(state, depth, player):
    if depth == 0 or state.check_game_over() != 0:
        return state.get_result(player)
    moves = state.get_possible_moves()
    if player == 1:
        best_value = -float("inf")
        for move in moves:
            state.make_move(move)
            value = mini_max(state, depth-1, 3-player)
            state.undo_move(move)
            best_value = max(best_value, value)
        return best_value
    else:
        best_value = float("inf")
        for move in moves:
            state.make_move(move)
            value = mini_max(state, depth-1, 3-player)
            state.undo_move(move)
            best_value = min(best_value, value)
        return best_value

# Define the function to find the best move
def find_best_move(state, player, depth):
    moves = state.get_possible_moves()
    if player == 1:
        best_value = -float("inf")
