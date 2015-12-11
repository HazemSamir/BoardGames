from games.connect4_models import Connect4Game
from game_controller import Controller
from views.sockets.server import TextServer
from games.tic_tac_toe_models import TicTacToeGame
from views.views import TextView
from AI.strategies import MinMax


if __name__ == '__main__':
    # controller_factory = ControllerFactory()
    view1 = TextView()
    view2 = TextServer()
    player1_strategy = MinMax()
    player2_strategy = view2
    game = TicTacToeGame(player1_strategy, player2_strategy)
    controller = Controller(game, view1, view2)
    controller.play()