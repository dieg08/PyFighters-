import socket, sys, json, Queue, GameServer, threading
"""
    A server that hosts a game between two clients in Pyfighters
"""
class GameServer(object): 

    #creates a GameServer, initializes it, 
    #and then starts listening for connections
    
    def main(self):
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
        t.start()

    #loops until there is no longer a connection
    def handle_connection(self, conn, status):
        while 1:
            # wait to accept a connection - blocking call 
            #print 'connected with '+ addr[0] + ':' + str(addr[1])
            data = conn.recv(4096)
            reply = 'Received: ' + data
            print reply 
            array = json.loads(data)
            if array[0] == 1:
                self.send1.put(array)
                print "Put " + str(array[0]) + " in queue 1"
            elif array[0] == 2:
                self.send2.put(array)
                print "Put " + str(array[0]) + " in queue 2"
            print 'player ' + str(array[0]) 
            print 'x position: ' + str(array[1])
            print 'y position: ' + str(array[2])
            print 'buttons pressed: ' + str(array[3])
            #thread.start_new_thread(self.sendNumber(conn, self.getNumber()), 0)
            self.sendNumber(conn, self.getNumber())
   
        

    #sends messages back to the clients
    def sendNumber(self, conn, number):
        message = number
        try:
            conn.send(message)
        except socket.error:
            print 'Send failed'
            sys.exit()

    def send(self, conn, number):
        message = None
        if number == 1:
            message = self.send2.get()
        elif number == 2:
            message = self.send1.get()
        packet = json.dumps(message)
        try:
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

    #closse the connection and shuts down server
    def close(self):
        self.conn.close()
        self.s.close()
    
    if __name__ == '__main__': main()
