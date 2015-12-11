import socket

class Messages:
    CLOSE = '__close__'
    INPUT = '__input__'
    SHOW = '__SHOW__'

if __name__ == 'main':
    host = raw_input(">>> enter host IP: ")
    if not host:
        host = socket.gethostname() # Get local machine name
    port = 23456                # Reserve a port for your service.
    s = socket.socket()
    try:
        s.connect((host, port))
        while True:
            rec = s.recv(1024)
            if rec.startswith(Messages.CLOSE):
                break
            elif rec.startswith(Messages.INPUT):
                rec = rec[len(Messages.INPUT):]
                msg = raw_input(rec)
                s.send(msg)
            elif rec.startswith(Messages.SHOW):
                rec = rec[len(Messages.SHOW):]
                print rec
    except Exception, err:
        print err
    
    s.close