import socket, sys, json, Queue, GameServer 
"""
    A server that hosts a game between two clients in Pyfighters
"""
class GameServer(object): 

    #creates a GameServer, initializes it, 
    #and then starts listening for connections
    def main():
        #The player
        NUMBER = 1
        server = GameServer.GameServer()
        server._init_()
        conn = server.listen()
        server.send(conn, server.getNumber(NUMBER))
    
    #initializes the GameServer
    def _init_(self):
        #Host IP and Port
        self.HOST = '127.0.0.1'
        self.PORT = 6969
        #creates queues to store the information sent by the players
        self.send1 = Queue.Queue()
        self.send2 = Queue.Queue()
        #Create the socket for a connection
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print 'Socket Created'
        #binds the port to address
        try:
            self.s.bind((self.HOST, self.PORT))
        except socket.error:
            print 'Failed to bind'
            sys.exit()
        print 'Bind successful'

    #method that listens for incoming connections
    def listen(self):
        status = None
        self.s.listen(10)
        conn, addr = self.s.accept()
        while 1:
            # wait to accept a connection - blocking call 
            print 'connected with '+ addr[0] + ':' + str(addr[1])
            data = conn.recv(4096)
            reply = 'Received: ' + data
            print reply 
            array = json.loads(data)
            if array[0] == 1:
                send1.put(array)
                print "Put " + str(array[0]) + " in queue 1"
                status = 1
            elif array[0] == 2:
                send2.put(array)
                print "Put " + str(array[0]) + " in queue 2"
                status = 1
            elif array[0] == 3:
                status = 0
            print 'player ' + str(array[0]) 
            print 'x position: ' + str(array[1])
            print 'y position: ' + str(array[2])
            print 'buttons pressed: ' + str(array[3])
            return conn

    #sends messages back to the clients
    def send(self, conn, number):
        message = None
        try:
            conn.send('hello world!')
        except socket.error:
            print 'Send failed'
            sys.exit()


    #assigns a player a number
    def getNumber(self, NUMBER):
        number = NUMBER
        message = str(number)
        if NUMBER == 1:
            NUMBER = 2
        elif NUMBER == 2:
            NUMBER = 1
        return message

    #closse the connection and shuts down server
    def close(self):
        conn.close()
        s.close()
    
    if __name__ == '__main__': main()
