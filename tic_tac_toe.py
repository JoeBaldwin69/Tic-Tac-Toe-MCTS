import random
import math



class TicTacToe:
    def __init__(self):
            self.state = ' ' * 9
            self.player = 'X'
    winning_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8), # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8), # Columns
        (0, 4, 8), (2, 4, 6) # Diagonals
    ]

    def print_board(self):
        print("-------------")
        print("| {} | {} | {} |".format(self.state[0], self.state[1], self.state[2]))
        print("-------------")
        print("| {} | {} | {} |".format(self.state[3], self.state[4], self.state[5]))
        print("-------------")
        print("| {} | {} | {} |".format(self.state[6], self.state[7], self.state[8]))
        print("-------------")

    def play_game(self):
        while not self.is_game_over():
            self.print_board()
            player_move = int(input("Player {}, enter your move: ".format(self.player)))
            while not self.is_valid_move(player_move):
                player_move = int(input("Invalid move. Try again: "))
            self.make_move(player_move)

        self.print_board()
        if self.winner():
            print("Player {} wins!".format(self.winner()))
        else:
            print("Tie game!")
        
      

    def is_game_over(self):
        return self.winner() or self.is_tie()
    
    def is_valid_move(self, move):
        return self.state[move-1] == ' '
    
    def make_move(self, move):
        self.state = self.state[:move-1] + self.player + self.state[move:]
        self.player = 'O' if self.player == 'X' else 'X'

    def winner(self):
        for combo in TicTacToe.winning_combinations:
            # Checks if the player has the same symbol in all the positions of any winning combinations
            if self.state[combo[0]] == self.state[combo[1]] == self.state[combo[2]] != ' ':
                return self.state[combo[0]]
        return None

    def is_tie(self):
        """Checks if the game is a tie"""
        for space in self.state:
            if space == ' ':
                return False
        return True

 

if __name__ == '__main__':
    game = TicTacToe()
    game.play_game()

