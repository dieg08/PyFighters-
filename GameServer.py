import socket, sys, json, Queue, GameServer, threading
"""
    A server that hosts a game between two clients in Pyfighters
"""
class GameServer(object): 
    """
    creates a GameServer, initializes it, 
    and then starts listening for connections
    """

    def main():
        #The player
        server = GameServer.GameServer()
        server._init_()
        while 1:
            server.listen()
    
    #initializes the GameServer
    def _init_(self):
        #Host IP and Port
        self.HOST = '127.0.0.1'
        self.PORT = 6969
        #creates queues to store the information sent by the players
        self.send1 = Queue.Queue()
        self.send2 = Queue.Queue()
        #player number assignment
        self.NUMBER = 1
        #variable to hold what character a player is
        self.one = None
        self.two = None
        #a variable to see how many threads there are
        self.thread_count = 0
        #Create the socket for a connection
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print 'Socket Created'
        #binds the port to address
        try:
            #self.s.bind((self.HOST, self.PORT))
            self.s.bind(('', self.PORT))
        except socket.error:
            print 'Failed to bind'
            sys.exit()
        print 'Bind successful'

    #method that listens for incoming connections
    def listen(self):
        status = 1
        self.s.listen(2)
        conn, addr = self.s.accept()
        t = threading.Thread(target=self.handle_connection, args=(conn, status,))
        try:
            t.start()
        except (KeyboardInterrupt, SystemExit):
            cleanup_stop_thread()
            sys.exit()

    #loops until there is no longer a connection
    def handle_connection(self, conn, status):
        state = 1
        num = self.getNumber()
        self.thread_count = self.thread_count + 1
        while True:
            # wait to accept a connection - blocking call 
            if self.thread_count > 1:
                if state == 1:
                    print "state 1"
                    player = conn.recv(1024)
                    #if num == 1:
                        #self.one = array[3]
                    #else:
                        #self.two = array[3]
                    self.sendNumber(conn, num)
                    char = None
                    if num == '1':
                        self.one = conn.recv(1024)
                        print "it get's here 1"
                    else:
                        self.two = conn.recv(1024)
                        print "it get's here 2"
                    if num == 1:
                        char = self.two
                    else:
                        char = self.one
                    if char != None:
                        self.sendChar(conn, char)
                        state = 2
                data = conn.recv(4096)
                reply = 'Received: ' + data
                print reply 
                if reply == 'Done':
                    close()
                try:
                    array = json.loads(data)
                    if array[0] == '1':
                        self.send1.put(array)
                        print "Put " + str(array[0]) + " in queue 1"
                    elif array[0] == '2':
                        self.send2.put(array)
                        print "Put " + str(array[0]) + " in queue 2"
                    print 'player ' + str(array[0]) 
                    self.send(conn, array[0])
                except ValueError:
                    print "Decoding JSON has failed"
                    sys.exit(0)

    #sends messages back to the clients
    def sendNumber(self, conn, number):
        message = number
        try:
            conn.send(message)
        except socket.error:
            print 'Send failed'
            sys.exit()

    def sendChar(self, conn, char):
        message = char
        try:
            if message != None:
                conn.send(message)
        except socket.error:
            print 'Send failed'
            sys.exit()

    def send(self, conn, number):
        message = None
        if number == '1':
            message = self.send2.get()
        elif number == '2':
            message = self.send1.get()
        packet = json.dumps(message)
        try:
            if packet != None:
                conn.send(packet)
        except socket.error:
            print 'Send failed'
            sys.exit()


    #assigns a player a number
    def getNumber(self):
        number = self.NUMBER
        message = str(number)
        if self.NUMBER == 1:
            self.NUMBER = 2
        elif self.NUMBER == 2:
            self.NUMBER = 1
        return message

    #close the connection and shuts down server
    def close(self):
        self.conn.close()
        #self.s.close()
    
    if __name__ == '__main__': main()
