# -*- coding: utf-8 -*-
import GameClient, pygame, sys, socket, WinScreen, json
"""
Created on Sun Mar 30 16:05:48 2014

The Initializing script for the game

@author: Will Stiles
@author: Diego Gonzalez
"""

"""
    Play the game
"""
player = 3

def main():
    #Keys pressed
    keysP = None
    #Create a game client
    client = GameClient.GameClient()
    #Initialize the connection with the server
    s = init()
    #Send a mesage to the server (broken)
    send(s, 0, 0, 0)
    #Catch a reply from the server, will contain the player
    reply = s.recv(1024)
    #The player number for this client
    player = reply
    #Print the player number (test)
    print str(player)

    #Start the game
    while client.ifWin() < 1:
        """
            Event Handling
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Exit the game
                sys.exit()
            if event.type == pygame.KEYDOWN and client.jump1Double < 2:
                client.jump1Double = client.jump1Double + 1
                keypressed = pygame.key.name(event.key)
                if keypressed == pygame.key.name(pygame.K_SPACE):
                    client.jump1Peak = client.player1Rect.top - 100
                    print client.jump1Peak
            client.keys = pygame.key.get_pressed()
            keysP = pygame.key.get_pressed()
        # Check for movement
        client.move()
        # Check for jumping
        client.jump()
        # Render the screen
        client.render()
        # Do attacks if necessary
        client.attack()
    if client.ifWin() == 1:
        WinScreen.winner("Player 1")
    elif client.ifWin() == 2:
        WinScreen.winner("Player 2")

"""
    Initialize the connection to the server
"""
def init():
    #Server IP and Port num
    host = '127.0.0.1'
    port = 6969
    player = 1
    #Try to create the socket and throw appropriate errs
    try: 
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error, msg:
        print 'Failed to create a socket'
        sys.exit()
    try:
        remote_ip = socket.gethostbyname( host )
    except socket.gaierror:
        #could not resolve host 
        print 'Hostname could not be resolved. Exiting'
        sys.exit()
    print  'IP address of ' + host + ' is ' + remote_ip
    s.connect((remote_ip, port))
    return s

"""
    Send information to the server
"""
def send(s, x, y, pressed):
    #Package to hold information to send to the server
    message = [player, x, y, pressed]
    packet = json.dumps(message)
    #Try sending the message and catch any errors
    try:
        s.sendall(packet)
    except socket.error:
        print 'Send failed'
        sys.exit

"""
    Call main method when script is run
"""
if __name__ == "__main__":
    main()
