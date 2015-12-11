from abc import ABCMeta, abstractmethod

class Strategy:
    __metaclass__ = ABCMeta    
    
    @abstractmethod
    def get_move(self, **args):
        pass

class _Play:
    def __init__(self, score=None, move=None):
        self.move = move
        self.score = score


class MinMax(Strategy):
    
    _MAX_DEPTH = 10
        
    def get_move(self, **args):
        '''
            compute the best cell to play in using minimax searching algorithm
        '''
        game = args['game']
        play = self._min_max(game, 0, self._max_score, self._min_score)
        return play.move
    

    def _min_max(self, game, depth, current_player_method, other_player_method):
        
        if game.finished() or self._MAX_DEPTH == depth + 1:
            if game.get_winner(): 
                return other_player_method(_Play(self._MAX_DEPTH - depth), 
                                           _Play(depth - self._MAX_DEPTH))
            else:   # tie game
                return _Play(0)
                
            
        best_play = _Play()
        for move in game.available_moves():
            temp_game = game.copy()
            if temp_game.play_into(move):
                play = self._min_max(temp_game, depth + 1, other_player_method,
                                     current_player_method)
                play.move = move
                best_play = current_player_method(best_play, play)
        
        return best_play
    
    def _min_score(self, play1, play2):
        if play1.score == None:
            return play2
        elif play2.score == None:
            return play1
        elif play1.score < play2.score:
            return play1
        else:
            return play2

    def _max_score(self, play1, play2):
        if play1.score == None:
            return play2
        elif play2.score == None:
            return play1
        elif play1.score > play2.score:
            return play1
        else:
            return play2
