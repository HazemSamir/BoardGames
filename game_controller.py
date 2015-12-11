from views.views import TextView
from AI.strategies import MinMax, Strategy
    
class Controller:
    
    def __init__(self, game, view1, view2):
        self.game = game
        self.view1 = view1
        self.view2 = view2
        
    def play(self):
        
        if self.view1 == self.view2:
            self.view1.show_board(self.game)
        else:
            self.view1.show_board(self.game)
            self.view2.show_board(self.game)
            
        while not self.game.finished():
            move = self.game.current_player.strategy.get_move(game=self.game)
            if not self.game.play_into(move):
                if self.view1 == self.view2:
                    self.view1.show_board(self.game)
                else:
                    self.view1.show_message('invalid move! play again')
                    self.view2.show_message('invalid move! play again')
            if self.view1 == self.view2:
                self.view1.show_board(self.game)
            else:
                self.view1.show_board(self.game)
                self.view2.show_board(self.game)
        
        if self.view1 == self.view2:
            self.view1.show_message('Game finished')
        else:
            self.view1.show_message('Game finished')
            self.view2.show_message('Game finished')
        
        
        winner = self.game.get_winner()
        if winner == None:
            msg = ("Draw no one won!")
        else:
            msg = ("Congratulations! " + winner.name + " won!")
        
        if self.view1 == self.view2:
            self.view1.close(msg)
        else:
            self.view1.close(msg)
            self.view2.close(msg)
""" 
class ControllerFactory:
    
    def create_controller(self, Game, number_of_players=1, view1,
                          view2, strategy1=MinMax, strategy2=MinMax):
        
        player1_strategy = strategy1()
        player2_strategy = strategy2()
        
        game = Game(player1_strategy, player2_strategy)
        return Controller(game, view1, view2)
"""