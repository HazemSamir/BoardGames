from copy import deepcopy

class Player:    
        
    def __init__(self, sympol, strategy, name=None):
        self.board = 0
        self.sympol = sympol
        self.strategy = strategy
        if name:
            self.name = name
        else:
            self.name = self.sympol + " Player"



class _Board:
    
    def __init__(self, width, height):
        self.board = [[None for i in range(width)] for i in range(height)]
        self.width = width
        self.height = height
        self.empty_cells = width * height
        self.sympol_cells = {}
    
    def get_xy(self, cell):
        if isinstance(cell, tuple):
            return cell
        else:
            return (cell / self.height, cell % self.width)
    
    def check_bounds(self, cell):
        x, y = self.get_xy(cell)
        return x < self.height and x >= 0 and y < self.width and y >= 0 
    
    def is_empty(self, cell):
        x, y = self.get_xy(cell)
        return self.board[x][y] == None 
    
    def play_into(self, sympol, cell):
        if self.check_bounds(cell) and self.is_empty(cell):
            x, y = self.get_xy(cell)
            self.board[x][y] = sympol
            self.empty_cells -= 1
            try:
                self.sympol_cells[sympol].append((x, y))
            except:
                self.sympol_cells[sympol] = [(x, y)]
            return True
        else:
            return False

    def get_sympol(self, cell):
        x, y = self.get_xy(cell)
        return self.board[x][y]

    def is_full(self):
        return self.empty_cells == 0
    
    def get_cells_of_sympol(self, sympol):
        try:
            return self.sympol_cells[sympol]
        except:
            return []


class TicTacToeGame:
    
    WIDTH = 3
    HEIGHT = 3
    CELLS_TO_WIN = 3
    
    def __init__(self, player1_strategy, player2_strategy, **kys):
        try:
            player1_sympol = kys['player1_sympol']
        except:
            player1_sympol = 'X'
        try:
            player2_sympol = kys['player2_sympol']
        except:
            player2_sympol = 'O'
        
        self.player_1 = Player(player1_sympol, player1_strategy)
        self.player_2 = Player(player2_sympol, player2_strategy)
        self.current_player = self.player_1
        self.board = _Board(self.WIDTH, self.HEIGHT)
        self.winner = None
        self.change_flag = False
    
    def play_into(self, cell):
        """
            @return: True: if the no error occurred when playing into input cell,
                    False: otherwise, (cell out of bounds, cell is not empty, 
                                        game is finished... etc)
            
            if the game is finished it switch players
        """
        if (not self.finished() and cell != None and 
            self.board.play_into(self.current_player.sympol, cell)):
            
            self._switch_players()
            self.change_flag = True
            return True 
        else:
            return False
        
    def _switch_players(self):
        if self.current_player == self.player_1:
            self.current_player = self.player_2
        else:
            self.current_player = self.player_1 
    
    def is_full(self):
        """
            @return: True if the board is full, else False
        """
        return self.board.is_full()
    
    def finished(self):
        return self.is_full() or self.get_winner()
    
    def get_sympol(self, cell):
        return self.board.get_sympol(cell)
    
    def available_moves(self):
        """
            @return: list of available moves in the game (empty cells)
        """
        available_moves_list = []
        for x in range(self.WIDTH):
            for y in range(self.HEIGHT):
                if self.board.is_empty((x, y)):
                    available_moves_list.append((x, y))
        return available_moves_list 
    
    def get_winner(self):
        """
            @return: Player Object of the player who won the game, 
                    None if no one won
            
            for efficiency the algorithm isn't run till the board is changed
            else returns a cached variable winner
            
        """
        if self.change_flag:
            self.change_flag = False
            if self._won(self.player_1):
                self.winner = self.player_1
            elif self._won(self.player_2):
                self.winner = self.player_2
        return self.winner
    
    def _won(self, player):
        for check_cell in self.board.get_cells_of_sympol(player.sympol):
                in_col = self._check_continous_cells(player, check_cell, 0, 1)
                in_row = self._check_continous_cells(player, check_cell, 1, 0)
                in_diagoal1 = self._check_continous_cells(player, check_cell, 1, 1)
                in_diagoal2 = self._check_continous_cells(player, check_cell, 1, -1)
                if ((in_row == self.CELLS_TO_WIN) or (in_col == self.CELLS_TO_WIN) or
                    (in_diagoal1 == self.CELLS_TO_WIN) or (in_diagoal2 == self.CELLS_TO_WIN)):
                    
                    return True
        return False 
    
    def _check_continous_cells(self, player, start_cell, x_increament, y_increament):
        counter = 0
        board = self.board
        x, y = start_cell
        while (x < board.height and x >= 0 and y >= 0 and 
               y < board.width and counter < self.CELLS_TO_WIN):
            
            if board.get_sympol((x, y)) != player.sympol:
                break
            else:
                counter += 1
                x += x_increament
                y += y_increament
        return counter
    
    def copy(self):
        """
            @return:  deep copy of the object
        """
        new_game = deepcopy(self)
        if self.current_player == self.player_1:
            new_game.current_player = new_game.player_1
        else:
            new_game.current_player = new_game.player_2
        return new_game
