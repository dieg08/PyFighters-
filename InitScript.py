# -*- coding: utf-8 -*-
import GameClient, pygame, sys, socket, WinScreen, json, errno 
from socket import error as socket_error
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

def main(socket):
    #Create a game client
    client = GameClient.GameClient()
    #Initialize the connection with the server
    s = socket
    #Send a mesage to the server (broken)
    send(s, 0, 0, 0)
    #Catch a reply from the server, will contain the player
    reply = s.recv(1024)
    #The player number for this client
    player = reply
    #Print the player number (test)
    print "Player: " + str(player)
    #Parameters of the message
    x = None
    y = None 
    keysp = None
    #Message that will be sent
    message = [x, y, keysp]
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
