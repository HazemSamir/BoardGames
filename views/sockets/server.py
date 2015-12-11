import socket
from views.views import TextView
from views.sockets.player_client import Messages

class TextServer(TextView):
    
    def __init__(self, host=socket.gethostname()):
        self.soc = socket.socket() 
        port = 23456
        self.soc.bind((host, port))
        self.soc.listen(5)                 # Now wait for client connection.
        self.client = None
    
    def get_move(self, **args):
        client = self.get_client()
        client.send(Messages.INPUT + 'enter move:')
        rec = client.recv(1024)
        return int(rec)
    
    def show_board(self, game, print_Number = False):
        board = ['\n']
        h_line = "+" * (game.WIDTH * 4 + 1)
        board.append(h_line + '\n')
        for x in range (game.HEIGHT):
            for y in range (game.WIDTH):
                board.append('| ')
                sympol = game.get_sympol((x,y))
                if sympol:
                    board.append(sympol + ' ')
                else:
                    board.append('  ')
            
            board.append('|\n')
            board.append(h_line + '\n')
        self.show_message(''.join(board))
    
    def show_message(self, msg):
        msg = Messages.SHOW + msg
        client = self.get_client()
        client.send(msg)
    
    def close(self, msg=''):
        self.show_message(msg)
        if self.client:
            self.client.send(Messages.CLOSE)
            self.client.close()
        self.soc.close()
    
    def get_client(self):
        if self.client:
            return self.client
        while True:
            self.client, addr = self.soc.accept()         # Establish connection with client
            print 'Got connection from', addr
            break
        return self.client