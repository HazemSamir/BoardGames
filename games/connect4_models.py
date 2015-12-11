from games.tic_tac_toe_models import TicTacToeGame
        

class Connect4Game(TicTacToeGame):
    
    WIDTH = 7
    HEIGHT = 6
    CELLS_TO_WIN = 4
    
    def __init__(self, player1_strategy, player2_strategy, **kys):
        TicTacToeGame.__init__(self, player1_strategy, player2_strategy, **kys)
        self.cols_capacity = [self.HEIGHT - 1 for i in range(self.WIDTH)]
        
    def play_into(self, cell):
        if (not self.finished() and cell < self.WIDTH and
            self.board.play_into(self.current_player.sympol, 
                                (self.cols_capacity[cell], cell))):
            self.cols_capacity[cell] -= 1
            self._switch_players()
            self.change_flag = True
            return True 
        else:
            return False
    
    def available_moves(self):
        available_moves_list = []
        for x in range(self.WIDTH):
            if self.cols_capacity[x] >= 0:
                available_moves_list.append(x)
        return available_moves_list