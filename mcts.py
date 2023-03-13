import math
import random
import tic_tac_toe as TicTacToe

class Node:
    def __init__(self, state, player):
        self.state = state
        self.player = player
        self.visits = 0
        self.score = 0
        self.children = []
        self.parent = None

    def is_fully_expanded(self):
        return len(self.children) == 9 - self.state.count(' ')

    def is_terminal(self):
        return any([self.is_winner('X'), self.is_winner('O'), self.is_tie()])

    def is_winner(self, player):
        """Checks if the current player has won"""
        for combo in TicTacToe.winning_combinations:
            # Checks if the player has the same symbol in all the positions of any winning combinations
            if self.state[combo[0]] == self.state[combo[1]] == self.state[combo[2]] == player:
                return True
        return False

    def is_tie(self):
        """Checks if the game is a tie"""
        for space in self.state:
            if space == ' ':
                return False
        return True

    def expand(self):
        possible_moves = [i for i, space in enumerate(self.state) if space == ' ']
        for move in possible_moves:
            new_state = self.state[:move] + self.player + self.state[move+1:]
            child = Node(new_state, 'O' if self.player == 'X' else 'X')
            child.parent = self
            self.children.append(child)

    def select(self):
        best_score = -1
        best_child = None
        for child in self.children:
            if child.visits == 0:
                return child
            else:
                score = child.score / child.visits + math.sqrt(2 * math.log(self.visits) / child.visits)
                exploration_value = math.sqrt(math.log(self.visits) / child.visits)
                total_score = score + exploration_value
            if total_score > best_score:
                best_score = total_score
                best_child = child
        return best_child

    def simulate(self):
        player = self.player
        state = self.state
        while not self.is_terminal():
            possible_moves = [i for i, space in enumerate(state) if space == ' ']
            move = random.choice(possible_moves)
            state = state[:move] + player + state[move+1:]
            player = 'O' if player == 'X' else 'X'
        if self.is_winner('X'):
            return 1 if self.player == 'X' else -1
        elif self.is_winner('O'):
            return 1 if self.player == 'O' else -1
        else:
            return 0

    def backpropagate(self, result):
        self.visits += 1
        self.score += result
        if self.parent:
            self.parent.backpropagate(result)


    # this function will return the best move for the current player 
    def play(state, player):
        root = Node(state, player)
        for i in range(1000):
            node = root
            # Selection
            while not node.is_terminal():
                if node.is_fully_expanded():
                    node = node.select()
                else:
                    # Expansion
                    child = random.choice([c for c in node.children if c.state not in [n.state for n in node.parent.children]])
                    node.children.append(child)
                    child.parent = node
                    node = child
                    break
            # Simulation
            result = node.simulate()
            # Backpropagation
            while node.parent:
                node.backpropagate(result)
                node = node.parent

        best_child = sorted(root.children, key=lambda c: c.visits)[-1]
        return best_child.state.index(player)

