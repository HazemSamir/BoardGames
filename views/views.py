from abc import ABCMeta, abstractmethod
from AI.strategies import Strategy 

class View(Strategy):
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def show_board(self, game, **args):
        pass
    
    @abstractmethod
    def show_message(self, msg):
        pass
    
    @abstractmethod
    def close(self, msg = ''):
        pass
        

def get_move(x, y, width):
    return y * width + x

class TextView(View):
    
    def get_move(self, **args):
        return input('enter move: ')
    
    def show_board(self, game, print_Number = False):
        print
        h_line = "+" * (game.WIDTH * 4 + 1)
        print h_line
        for x in range (game.HEIGHT):
            for y in range (game.WIDTH):
                print "|",
                sympol = game.get_sympol((x,y))
                if (sympol == None):
                    print " ",
                else:
                    print sympol,
            print "|" 
            print h_line
    
    def show_message(self, msg):
        print msg
    
    def close(self, msg=''):
        print msg